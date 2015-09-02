from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def enter(request):
    return render(request, 'enter.html',{})


def individual(request):
    return render(request, 'individual_view.html',{})

def upload(request):
    return render(request, 'upload_view.html',{})