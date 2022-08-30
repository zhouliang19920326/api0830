# 一、还原手工操作
#
# 所谓爬取页面图片，正常人手动操作可以分为两步：
#
# 1.打开页面
#
# 2.选中图片下载到指定文件夹
#
# 用代码实现的话可以节省掉每次下载图片的操作，运行代码实现批量下载。
#
# 二、设计代码实现
#
# 步骤一：导入相关库操作

# import urllib #导入urllib包
#
# import urllib.request#导入urllib包里的request方法
#
# import re #导入re正则库
#
# # 步骤二：定义解析页面 load_page（）
# #
# # 这个函数实现打开传入的路径并将页面数据读取出来，实现代码，包括发送请求，打开页面，获取数据。
# #
# # 代码实现：
#
# def load_page(url):
#
#     request=urllib.request.Request(url)#发送url请求
#
#     response=urllib.request.urlopen(request)#打开url网址
#
#     data=response.read()#读取页面数据
#
#     return data#返回页面数据
#
# # 步骤三：定义get_image()函数
# #
# # 首先利用正则表达式匹配图片路径并存到数组中。
# #
# # 其次遍历数组实现图片下载操作。
# #
# # 代码实现：
#
# def get_image(html):
#
#     regx=r'http://[\S]*jpg' #定义正则匹配公式
#
#     pattern=re.compile(regx)#构造匹配模式，速度更快
#
#     get_image=re.findall(pattern,repr(html))#repr（）将内容转化为字符串形式，findall列表形式展示正则表达式匹配的结果
#
#     num=1 #定义变量控制循环
#
#     for img in get_image: #定义变量遍历数组
#
#         image=load_page(img)#将图片路径传入加载函数
#
#         with open('D:\\photo1\\%s.jpg'%num,'wb') as fb: #以只读方式打开图片并命名
#
#             fb.write(image) #写入内容
#
#             print('正在下载第%s张图片'%num)
#
#         num=num+1 #变量递增
#
#     print("下载完成")

# 步骤四：函数调用

import urllib.request

import ssl

ssl._create_default_https_context = ssl._create_stdlib_context

# 定义保存函数
def saveFile(data):
    path = "D:\\photo1\\carhome.txt"
    f = open(path, 'wb',)
    f.write(data)
    f.close()


# 网址
url = "https://car.autohome.com.cn/photo/55530/53/7359112.html"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/51.0.2704.63 Safari/537.36'}
req = urllib.request.Request(url=url, headers=headers)

res = urllib.request.urlopen(req)

data = res.read()

# 也可以把爬取的内容保存到文件中
saveFile(data)

# data = data.decode('utf-8')
# 打印抓取的内容
print(data)

# 打印爬取网页的各类信息
print(type(res))
print(res.geturl())
print(res.info())
print(res.getcode())

#调用函数
# if __name__ == '__main__':
#     url='https://car.autohome.com.cn/photo/55530/53/7359111.html'
#     # url = 'http://p.weather.com.cn/2019/10/3248439.shtml'
#     #传入url路径
#
#     html=load_page(url)#加载页面
#
#     get_image(html)#图片下载

# 关键单词释义

# 如果第一次接触爬虫代码，相信有几个单词大家很陌生，为了方便记忆我把他们归类到一起加深印象，你也可以拿出一张白纸试着努力回忆着。
#
# 1.爬虫协议库ulrlib、urllib.request
#
# 2.正则匹配库rb
#
# 3.发送请求方法request（）
#
# 4.打开页面方法urlopen（）
#
# 5.读取数据方法read（）
#
# 6.正则表达式-所有图片【\S】*.jpg
#
# 7.匹配模式定义compile（）
#
# 8.查找匹配findall（）
#
# 9.循环遍历语句 for a in b
#
# 10.打开文件 并命名 with open（）... as fb
#
# 11.写到... write*()
#
# 12.输出语句 print（）