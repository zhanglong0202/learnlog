# 1.在本地目录创建文件夹用来存放当天视频资料
# 2.从网络链接中下载视频种子
# 3.用种子文件自动下载视频到文件夹中
import os
import time
import urllib
import easygui as ui


def make_dirs(path):
    try:
        os.makedirs(path)
    except Exception as err:
        print(err)


def creat_dir(path=''):
    # down_dir = ui.diropenbox()
    # path = down_dir
    path = r"F:\learn in blackhorse\就业班\a\b"
    make_dirs(path)


def download_bt():
    pass


def download_doc():
    pass


def main():
    creat_dir()
    download_bt()
    download_doc()


if __name__ == '__main__':
    main()
