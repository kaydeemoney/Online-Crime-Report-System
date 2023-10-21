from django.urls import path
from .import views

urlpatterns=[
    path("",views.index,name="index"),
    path("login/",views.LoginForm,name="login"),
    path("logout/",views.logout,name="logout"),
    path('register/',views.RegisterForm,name='RegisterForm'),
    path("contact/",views.contact,name="contact"),
    path("missing/",views.missing,name="missing"),
    path("wanted/",views.wanted,name="wanted"),
    path("crime_stories/",views.crime_stories,name="crime_stories"),
    path("help/",views.help,name="help"),
    path("complaint_form/",views.complaint_form,name="complaint_form"),
    path("Admin/",views.Admin,name="Admin")

    

]