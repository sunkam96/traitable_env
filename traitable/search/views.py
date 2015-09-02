from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def search(request):
    context = {'title':'Search Platform'}
    return render(request, 'search.html',context)