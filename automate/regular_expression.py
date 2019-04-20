# 功能需求
# 正则表达式
#
# 导入模块
import re


def re_match():
    phone = '0752-2238315'
    re_result = re.match(r'\d\d\d\d-\d\d\d\d\d\d\d', phone)

    print(re_result, '\n', re_result[0])


def re_search():
    # ********************************
    # 1.用import re导入正则表达式模块

    # 2.用re.compile()函数创建一个regex对象
    phone_regex = re.compile(r'\d\d\d\d-\d\d\d\d\d\d\d')

    # 3.用regex对象的search()方法出入想要查找的字符串，他会返回一个match对象
    result = phone_regex.search('我的电话号码是: 0752-2238315')

    # 4.调用match对象的group()方法，返回实际匹配文本的字符串
    print('search方法获得结果', result.group())
    # ************************************
    # 利用括号分组
    # phone_regex = re.compile(r'(\d\d\d\d)-(\d\d\d\d\d\d\d)')
    # 花括号可以输入匹配次数
    phone_regex = re.compile(r'(\d{4})-(\d{7})')
    result = phone_regex.search('我的电话号码是: 0752-2238315')
    print('获取分组的匹配结果:', result.group(1))
    print('获取分组的匹配结果:', result.group(2))
    print('获取分组的匹配结果:', result.group(0))
    print('获取所有分组的匹配结果:', result.groups())


def pipeline():
    # 管道符号 | ,匹配左边或者右边的一个
    hero_regex = re.compile(r'batman|superman')
    result = hero_regex.search('superman is so strong!')
    print(result.group())
    # ? 匹配前一个字符存在或不存在都匹配
    hero_regex = re.compile(r'Bat(wo)?man')
    result = hero_regex.search('Batman is live in Gotham city')
    print(result.group())


def main():
    # re_match()
    re_search()
    pipeline()


if __name__ == '__main__':
    main()
