from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    peoples=[{'name':'abcs','age':20},
             {'name':'abcs','age':50},
             {'name':'abcs','age':90},
             {'name':'abcs','age':15}
             ]
    text="""lorem*10hbajhjfnknw qhj,hnbjfwjklqNKRQDwnmefjmdsabghkhjL<MMfbjwkqejakekmgmdsfhhklqwal;MFDB"""
    return render(request,"index.html",context={'peoples':peoples,'text':text})
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def start(request):
    return HttpResponse("appjoaj kdfjak")
