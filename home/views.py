from django.shortcuts import render, HttpResponse
from pprint import pprint
import random

# Create your views here.
def index(request):
    # print(request)
    # print(type(request))
    # pprint(request.META)
    return HttpResponse('Welcome to Django !')
    
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
    