#!/usr/bin/
# -*- coding: UTF-8 -*-

import os
import shutil
import filetype
def get_filepath_by_type(root_path, s, all_files = []):
    """
    递归函数，遍历该文档目录和子目录下的所有指定类型的文件，获取其path
    @root_path 根目录文件
    @str 文件后缀
    @return all_files 返回目录和子目录下的所有文件路径
    """
    files = os.listdir(root_path)
    for f in files:
        if not os.path.isdir(root_path + '\\' + f):
            if f.split(".")[1] == s:
               all_files.append(root_path + '\\' + f)
        else:
            get_filepath_by_type((root_path+'\\'+f),s,all_files)
    return all_files

def delete_file(root_path):
    """
    递归某文件夹，删除该文件夹下所有的文件和子文件夹
    @root_path 根目录文件
    """
    filelist = os.listdir(root_path)  # 列出该目录下的所有文件名
    for f in filelist:
        filepath = os.path.join(root_path, f)  # 将文件名映射成绝对路劲
        if os.path.isfile(filepath):  # 判断该文件是否为文件或者文件夹
            os.remove(filepath)  # 若为文件，则直接删除
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath, True)  # 若为文件夹，则删除该文件夹及文件夹内所有文件

def get_mime(fileNames):

    '''根据文件路径，自动获取文件名称和文件mime类型'''
    filepath = fileNames
    kind = filetype.guess(filepath)
    if kind is None:
        print('Cannot guess file type!')
        return
    # 媒体类型，如：image/png
    mime_type = kind.mime
    return mime_type


