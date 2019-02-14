from django.shortcuts import render, HttpResponse
from pprint import pprint
import random
from datetime import datetime

# Create your views here.
def index(request):
    # print(request)
    # print(type(request))
    # pprint(request.META)
    # return HttpResponse('Welcome to Django !')
    return render(request, 'index.html')
    
def dinner(request):
    menus = ['삼겹살', '칼국수', '치킨', '족발', '초밥']
    pick = random.choice(menus)
    return render(request, 'dinner.html', {'menus' : menus, 'pick' : pick})

def hello(request, name):
    return render(request, 'hello.html', {'name' : name})
    
def cube(request, num):
    num = int(num)
    result = num**3
    return render(request, 'cube.html', {'num' : num, 'result' : result })
    
def ping(request):
    return render(request, 'ping.html')
    
def pong(request):
    print(request.GET)
    data = request.GET.get('data')
    return render(request, 'pong.html', {'data': data})
    
def user_new(request):
    return render(request, 'new.html')
    
def user_create(request):
    nickname = request.POST.get('nickname')
    pwd = request.POST.get('pwd')
    return render(request, 'create.html', {'nickname' : nickname, 'pwd' : pwd})
    
def template_example(request):
    my_list = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucmber', 'mango']
    empty_list = []
    datetimenow = datetime.now()
    return render(request, 'template_example.html',
                    {'my_list' : my_list, 'my_sentence' : my_sentence, 
                    'messages' : messages, 'empty_list' : empty_list,
                    'datetimenow' : datetimenow
                    })