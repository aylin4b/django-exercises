from django.shortcuts import render

# Create your views here.
from django.forms import SlugField
from django.shortcuts import render
from .models import Example
from django.http import HttpResponse, JsonResponse


def index(req):
    examples = Example.objects.all()
    
    context ={
        'examples':examples
    }
    return render(req, 'blogApp/index.html', context)


def detail(req, pk):
    examples = Example.objects.get(slug=pk)
    
    context ={
        'examples':examples
    }
    return render(req, 'blogApp/detail.html', context)