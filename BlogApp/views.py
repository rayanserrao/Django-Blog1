from django.shortcuts import render

# Create your views here.

def index(request):
    title="Home Page"
    return render (request,'index.html',{'title': title})


def about(request):
    return render(request,'about.html')

def databse(request):
    return render (request,'database.html')

def socketprogram(request):
    return render(request,'socketprg.html')

def pythonrule(request):
    return render(request,'basic.html')
