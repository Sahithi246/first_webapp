from django.urls import path
from . import views
urlpatterns=[
path("register",views.register,name="register"),
path("register_t",views.register_t,name="register_t"),
path("login",views.login,name="login"),
path("dashboard",views.dashboard,name="dashboard"),
path("login_user",views.login_user,name="login_user"),
path("my_learning",views.my_learning,name="my_learning"),
path("my_mentors",views.my_mentors,name="my_mentors"),
path("assignments",views.assignments,name="assignments"),
path("mentors",views.mentors,name="mentors")


]

