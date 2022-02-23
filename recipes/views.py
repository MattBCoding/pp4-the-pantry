from django.shortcuts import render, HttpResponse

# Create your views here.
def say_hello(request):
    return HttpResponse("Hello!")

def home(request):
    context = {}
    return render(request, 'index.html/', context) 