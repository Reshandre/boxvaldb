from django.shortcuts import render

# Create your views here.
def index(request):
    message = "This is the masters location"
    return render (request, 'masters/index_simple.html', {'message':message})