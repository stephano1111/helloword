from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homePageView(request):
    return render(request, 'about.html', {})
    #return HttpResponse('About');
