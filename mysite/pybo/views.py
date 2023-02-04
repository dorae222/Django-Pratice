from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(requet):
    return HttpResponse("pybo 페이지에 접근하셨습니다.")

def test(request):
    return HttpResponse('<h1>test page에 접근하셨습니다<\h1>')
