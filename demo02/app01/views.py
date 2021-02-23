from django.shortcuts import render, HttpResponse, redirect, reverse


# Create your views here.
def test(request, xx):
    print(xx)
    return HttpResponse('test')


def testadd(request, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse('testadd')


def home(request):
    print(reverse('other_name'))
    return render(request, 'home.html')


def function(request):
    return HttpResponse('function')
