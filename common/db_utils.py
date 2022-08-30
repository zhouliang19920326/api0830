from common.logger import *
from common.config import *

logger = Logger().getlog()

from pymysql import *


class MysqlHelp(object):
    """mysql常用方法的封装"""

    def __init__(self, dbdatabase):
        config = Config()

        self.db = None
        self.cursor = None
        self.host = config.dbhost
        self.username = config.dbusername
        self.password = config.dbpassword
        self.port = config.dbport
        self.database = dbdatabase
        self.config = {
            'host': str(self.host),
            'user': self.username,
            'passwd': self.password,
            'port': int(self.port),
            'db': self.database
        }
        self.conn = Connection(**self.config)  # 获取连接对象
        self.cr_obj = self.conn.cursor()  # 获取cursor对象

    def get(self, field, table_name, num):
        self.cr_obj.execute("select %s from %s" % (field, table_name))
        if num == 1:
            return self.cr_obj.fetchone()  # 获取一数据
        else:
            return self.cr_obj.fetchall()  # 获取所有的数据

    def insert(self, table_name, field_name, field_value):
        st = ""
        for i in field_name:
            if i == field_name[-1]:
                st += "".join(i + ")")
            elif i == field_name[0]:
                st += "".join("(" + i + ",")
            else:
                st += "".join(i + ",")
        field_name = st
        sql = "insert into {}{} values{}".format(table_name, field_name, field_value)
        logger.info(sql)
        ret = self.cr_obj.execute("insert into {}{} values{}".format(table_name, field_name, field_value))
        logger.info(ret)

    def update(self, table_name, field):
        field_name = field["field_name"]
        field_value = field["field_value"]
        c_field = field["c_field"]
        v_field = field["f_field"]

        field_value = "'" + field_value + "'"
        ret = self.cr_obj.execute(
            "update {} set {}={} where {}={}".format(table_name, field_name, field_value, c_field, v_field))
        logger.info(ret)

    def delete(self, table_name, field_name, field_value):
        field_value = "'" + field_value + "'"
        if (len(field_value) > 0):
            ret = self.cr_obj.execute("delete from %s where %s = %s" % (table_name, field_name, field_value))
            self.conn.commit()
            return ret

    def query(self, table_name, field_name, field_value):
        self.cr_obj.execute("SELECT * from %s where %s = '%s' " % (table_name, field_name, field_value))
        index = self.cr_obj.description
        result_data = []
        for res in self.cr_obj.fetchall():
            row = {}
            for i in range(len(index)):
                row[index[i][0]] = res[i]
                result_data.append(row)
        return result_data

    def close(self):
        self.conn.commit()
        self.cr_obj.close()
        self.conn.close()


if __name__ == '__main__':
    ret2 = MysqlHelp('auth-center').query('auth_account', 'phone', 18222222220)
    account = ret2[0]['account_no']
    userCenter = MysqlHelp('user-center').query('user_enterprise', 'account_no', account)
    user_enterpriseID = userCenter[0]['id']
    # 得到shop-center
    userCenter = MysqlHelp('shop-center').query('shop_merchant_shop', 'user_no', account)
    shop_no = userCenter[0]['shop_no']
    # 删除 user_enterprise_certificate 表
    user_enterprise_certificate = MysqlHelp('user-center').delete('user_enterprise_certificate', 'enterprise_id',
                                                                  str(user_enterpriseID))
    # 删除 user_enterprise
    user_enterprise = MysqlHelp('user-center').delete('user_enterprise', 'account_no', str(account))
    # 删除 shop_address
    del_shop_address = MysqlHelp('shop-center').delete('shop_address', 'user_no', str(account))
    # 删除 shop_extra
    del_shop_extra = MysqlHelp('shop-center').delete('shop_extra', 'shop_no', str(shop_no))
    # 删除 shop_merchant_shop
    del_shop_merchant_shop = MysqlHelp('shop-center').delete('shop_merchant_shop', 'user_no', str(account))
    # 删除 acccount
    del_auth_account = MysqlHelp('auth-center').delete('auth_account', 'phone', '18222222220')
