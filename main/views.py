from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import asyncio
# import telegram
import json
# import pyrebase
import requests
from . import fb


# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, 'index.html')


def sendView(request):
    return render(request, 'Chatbot.html')


@csrf_exempt
def sendCtrl(request, id):
    if request.method == "POST":
        print(request.POST)
        body = json.loads(request.body.decode('utf-8'))

        message = body['message']

        # async def main():  # 실행시킬 함수명 임의지정
        #     token = "6035558120:AAE0Xkgv5OY8_fpLtEF9KqWO_QU5Wnamdr8"
        #     bot = telegram.Bot(token=token)
        #     await bot.send_message(id, message)
        #
        # asyncio.run(main())  # 봇 실행하는 코드
        # return redirect('/')

    else:
        return render(request, 'Chatbot.html')


def markHospital(request):
    return render(request, 'map.html')