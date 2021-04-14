from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def login(request):
	if request.method=="POST":
		username=request.POST.get('username')
		password=request.POST['password']

		user=auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request,user)
			return render(request,'accounts/login_user.html')

		else:
			messages.info(request,"invalid credentials")
			return redirect("login")
	else:
		return render(request,'accounts/login.html')


def register(request):

	if request.method=="POST":
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		username=request.POST['username']
		password=request.POST['password']
		password2=request.POST['password2']
		email=request.POST['email']

		if password==password2:
			if User.objects.filter(username=username).exists():
				messages.info(request,"Username is already taken")
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.info(request,"Email already registered")
				return redirect('register')
			else:
				user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
				user.save();
				return redirect("login")
				
		else:
			print("Password not matching")
		return redirect('/')
	else:
		return render(request,'accounts/register.html')



def register_t(request):

	if request.method=="POST":
		first_name=request.POST['first_name']
		subject=request.POST['subject']
		last_name=request.POST['last_name']
		username=request.POST['username']
		password=request.POST['password']
		password2=request.POST['password2']
		email=request.POST['email']

		if password==password2:
			if User.objects.filter(username=username).exists():
				messages.info(request,"Username is already taken")
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.info(request,"Email already registered")
				return redirect('register')
			else:
				user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name,subject=subject)
				user.save();
				return redirect("login")
				
		else:
			print("Password not matching")
		return redirect('/')
	else:
		return render(request,'accounts/register_t.html')

def dashboard(request):
	return render(request,'accounts/dashboard.html')

def login_user(request):
	return render(request,'accounts/login_user.html')

def my_learning(request):
	return render(request,'accounts/my_learning.html')

def my_mentors(request):
	return render(request,'accounts/my_mentors.html')

def assignments(request):
	return render(request,'accounts/assignments.html')

def mentors(request):
	return render(request,'accounts/mentors.html')