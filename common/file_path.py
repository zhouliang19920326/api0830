import os

# 获取当前项目路径
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

# 测试输出报告目录
report_data_path = os.path.join(project_path, 'Outputs', 'report_data')
report_dir = os.path.join(project_path, 'Outputs', 'reports')
# 日志文件路径
log_dir = os.path.join(project_path, 'Log')

# 测试数据
date_dir = os.path.join(project_path, 'testdata')
# 图片路径
img_path = os.path.join(project_path, 'testdata', 'img', 'product.jpg')
# 视频路径
video_path = os.path.join(project_path, 'testdata', 'Videos', '1.mp4')
# 全局变量文件
variable_data_path = os.path.join(project_path, 'testdata', 'variable_data.yaml')


if __name__ == '__main__':
    print(os.path.realpath(__file__))
    print(os.path.split(os.path.realpath(__file__)))
    print(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0])
    print(date_dir)
    print(project_path)
    print(variable_data_path)
    print(log_dir)


