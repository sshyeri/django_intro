from django.shortcuts import render
from datetime import datetime
import requests
import random
import os

# Create your views here.
today = datetime.now().date()

def index(request):
    return render(request, 'utilities/index.html')
    
def bye(request):
    dday = datetime(2020,2,28).date()
    td = (dday - today).days
    return render(request, 'utilities/bye.html', {
                'today': today, 'dday' : dday, 'td': td})
                
def graduation(request):
    dday = datetime(2019, 5, 28).date()
    td = (dday - today).days
    return render(request, 'utilities/graduation.html', {
                'today': today, 'dday' : dday, 'td': td})
                
def imagepick(request):
    return render(request, 'utilities/imagepick.html')
    
# def today(request):
#     key = "80f1ea7bdfb5a7f94a02608b259e1b89"
#     url = f"https://api.openweathermap.org/data/2.5/weather?q=Seoul,kr&lang=kr&appid={key}"
#     response = requests.get(url).json()
#     weather = response["weather"][0]["description"]
#     temp = response["main"]["temp"]
#     temp -= 273.15
#     temp_min = response["main"]["temp_min"]
#     temp_min -= 273.15
#     temp_max = response["main"]["temp_max"]
#     temp_max -= 273.15
#     return render(request, 'utilities/today.html', {'weather' : weather,
#                     'temp' : int(temp), 'temp_min' : temp_min, 'temp_max' : temp_max})
     
fonts =['short', 'utopia', 'rounded', 'acrobatic', 'alligator']

def ascii_new(request):
    
    return render(request, 'utilities/ascii_new.html', {'fonts' : fonts})
    
def ascii_make(request):
    text = request.GET.get('text')
    font = request.GET.get('font')
    url = f"http://artii.herokuapp.com/make?text={text}&font={font}"
    res = requests.get(url).text
    return render(request, 'utilities/ascii_make.html', {'res' : res})
    
def original(request):
    font = random.choice(fonts)
    url = f"http://artii.herokuapp.com/make?text=Translator&font={font}"
    res = requests.get(url).text
    return render(request, 'utilities/original.html', {'res' : res})
    
def translated(request):
    font = random.choice(fonts)
    url = f"http://artii.herokuapp.com/make?text=Translator&font={font}"
    res = requests.get(url).text
    kor = request.GET.get('kor')
    
    naver_client_id = os.getenv("NAVER_CLIENT_ID")
    naver_client_secret = os.getenv("NAVER_CLIENT_SECRET")
    papago_url = "https://openapi.naver.com/v1/papago/n2mt"

    headers = {
        "X-Naver-Client-Id": naver_client_id,
        "X-Naver-Client-Secret": naver_client_secret
    }
    data = {
        "source": "ko",
        "target": "en",
        "text": kor
    }
    papago_response = requests.post(papago_url, headers=headers, data=data).json()

    reply_text = papago_response["message"]["result"]["translatedText"]
    print(reply_text)
    return render(request, 'utilities/translated.html',{'res' : res, 
                'kor' : kor, 'reply_text' : reply_text})