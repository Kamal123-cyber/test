from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'bookstore/base.html')

def index(request):
	return httpresponse