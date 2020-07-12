from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# user: trydeploydjango, email:9109kumar@gmail.com , pass:codewithdjango

def home(request):
    return render(request, 'dplyapp/index.html')
