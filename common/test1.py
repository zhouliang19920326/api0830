

import os


# def getPath(x:str):
#     path1 = os.getenv(x)
#     return path1

def getPath(x:str):
    #words = os.getenv(x)
    words = os.environ.get(x)
    print(type(words),words)
    f="C:\\Users\\EDY\\Desktop\\var.txt"
    with open(f, "w") as file:  # ”w"代表着每次运行都覆盖内容
        file.write(words)
    return words

d = getPath('hostname22')
print(type(d),d)