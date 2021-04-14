from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Destination
from django.contrib.auth.models import User,auth
# Create your views here.
def index(request):
	dests=Destination.objects.all()
	return render(request,'my_app/index.html',{'dests':dests})
