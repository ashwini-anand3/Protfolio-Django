from django.shortcuts import render
from .models import Blog

# Create your views here.
def home(request):
	obj = Blog.objects.all()
	return render(request,'blogs/index.html',{'obj':obj})

def details(request,id):
	data = Blog.objects.filter(pk=id)
	return render(request,'blogs/details.html',{'data':data})