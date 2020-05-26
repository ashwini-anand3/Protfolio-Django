from django.shortcuts import render
from .models import Jobs

# Create your views here.
def jobs_home(request):
	obj = Jobs.objects.all()
	return render(request,'jobs/index.html',{'obj':obj})