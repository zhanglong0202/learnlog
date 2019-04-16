# 程序启动文件,测试导包功能
import os


def main():
    os.system("pip install bs4")
    os.system("pip install requests")
    import spider.crawler_python as spider
    spider.main()


if __name__ == '__main__':
    main()
