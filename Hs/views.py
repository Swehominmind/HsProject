from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'Hs/index.html', context={
        'title': 'Hs首页',
        'welcome': '欢迎访问Kevin和Kass的炉石PJ首页'
    })
