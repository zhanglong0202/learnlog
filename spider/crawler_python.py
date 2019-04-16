# 导入requests 用来读取网页
# 导入bs4 用来使用网页格式剖析网页,获取元素信息
from bs4 import BeautifulSoup
import requests as rq
import os

# 设置固定变量
# 固定的网页地址
path = "F:\learn in blackhorse\就业班"
url = 'http://python20.top'


def main():
    # 使用get方法获取到网页
    data = rq.get(url)

    # 修改为utf-8解码方式,防止乱码
    data.encoding = 'utf-8'
    # print(data.text)

    # 使用beautifulSoup 对网页进行剖析
    soup = BeautifulSoup(data.text, 'html.parser')

    # 使用选择器选取到a标签下的元素内容
    link = soup.select('.box a')
    # print(link)
    for i in link:
        # down_bt(i)
        bt_path = i['href']
        bt_list = bt_path.split('/')
        print(bt_list[-1])
        down_path = os.path.join(path, bt_list[-1])
        if not os.path.exists(down_path):
            down_bt(bt_path, down_path)


def down_bt(bt_path, down_path):
    bt_url = url + bt_path
    print('开始下载文件',bt_path)
    bt_data = rq.get(bt_url)

    # 不知道什么作用的代码
    bt_data.raise_for_status()

    with open(down_path, 'wb') as f:
        for chunk in bt_data.iter_content(100000):
            f.write(chunk)
        else:
            print('下载完成!')


if __name__ == '__main__':
    main()
