from django.shortcuts import render

# Create your views here.

def biryani(request):
    return render(request,'biryani.html')

def curd(request):
    return render(request,'curd.html')
