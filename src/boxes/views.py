from django.shortcuts import render
from django.http import JsonResponse,HttpResponse

# Create your views here.

def index(request):
    # return JsonResponse({'text':'Another hello world'})
    return HttpResponse({"content":'This is a content'})
