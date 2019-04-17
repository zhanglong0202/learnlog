from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def user_login(request):

    res = '<div style = "text_align:center"><H1>欢迎登录</H1></div>'
    return HttpResponse(res)