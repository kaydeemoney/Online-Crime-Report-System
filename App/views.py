from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import CreateUserForm
from django.contrib.auth.models import Group
from .models import *
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
import random
from django.conf import settings
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, 'App/home.html')


def missing(request):
    missing_persons = missingperson.objects.all()
    return render(request, 'App/missing.html', {'missing_persons': missing_persons})


def wanted(request):
    wanted_person = wantedperson.objects.all()
    return render(request, 'App/wanted.html', {'wanted_persons': wanted_person})


def crime_stories(request):
    crime_stories = crimestories.objects.all()
    return render(request, 'App/crime_stories.html', {'crime_stories': crime_stories})

@login_required(login_url='/login')
def complaint_form(request):
   
    if request.method == "POST":
        complaint_type = request.POST.get('complaint_type','')
        crime_place = request.POST.get('crime_place','')
        crime_in_detail = request.POST.get('crime_in_detail','')
        first_name = request.POST.get('first_name','')
        middle_name = request.POST.get('middle_name','')
        last_name = request.POST.get('last_name','')
        age = request.POST.get('age','')
        gender = request.POST.get('gender','')
        date_of_birth = request.POST.get('date_of_birth','')
        email_id = request.POST.get('email_id','')
        mobile_no = request.POST.get('mobile_no','')
        house_no = request.POST.get('house_no','')
        permanent_address = request.POST.get('permanent_address','')
        landmark = request.POST.get('landmark','')
        state = request.POST.get('state','')
        distict_place = request.POST.get('distict_place','')
        
        info = ComplaintRegister(complaint_type=complaint_type, crime_place=crime_place, crime_in_detail=crime_in_detail, first_name=first_name,
                                 middle_name=middle_name, last_name=last_name, age=age, gender=gender, date_of_birth=date_of_birth,email_id=email_id, mobile_no=mobile_no, house_no=house_no,permanent_address=permanent_address,
                                 landmark=landmark, state=state, distict_place=distict_place)
        
        info.save()
        return render(request, 'App/complaint_register.html')

    else:
        
        return render(request, 'App/complaint_register.html')


def contact(request):
    return render(request, 'App/contact.html')


def help(request):
    return render(request, 'App/help.html')


def RegisterForm(request):
    form = CreateUserForm()
    if request.method == 'POST':
        get_otp = request.POST.get('otp')
        if get_otp:
            get_usr = request.POST.get('usr')
            usr = User.objects.get(username=get_usr)

            if int(get_otp) == UserOTP.objects.filter(user_name=usr).last().otp:
                    usr.is_active=True
                    group=Group.objects.get(name='User')
                    usr.groups.add(group)
                    usr.save()
                    messages.success(request, f'Account is created for {usr}')
                    return redirect('/login')
            else:
                    messages.error(request, f'you enter wrong otp')
                    return render(request, 'App/register.html', {'otp': True, 'usr': usr})

        form = CreateUserForm(request.POST)
        if form.is_valid():

            
            if User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, 'App/register.html', {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            
            

            else:
               form.save()
               username = form.cleaned_data.get('username')            
               usr=User.objects.get(username=username)
               usr.is_active=False
               usr.save()
               usr_otp = random.randint(100000, 999999)
               UserOTP.objects.create(user_name=usr, otp=usr_otp)

               email_subject = 'Activate Account'
               message = f"Hello {username} your otp is {usr_otp}\n Thanks for Register."
            
               send_mail(email_subject,
                      message,
                      settings.EMAIL_HOST_USER,
                      [usr.email],
                      fail_silently=False)
               return render(request, 'App/register.html', {'otp': True, 'usr': usr,'error_message': f'otp send to {usr.email}'})
        
        return render(request, 'App/register.html',{'form': form,'error_message': 'Incorrect username and password.'})

    else:
        
        return render(request, 'App/register.html', {'form': form})







# def LoginForm(request):
#     # if this is a POST request we need to process the form data
#     template = 'App/LoginForm.html'

#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = RegisterForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             if User.objects.filter(username=form.cleaned_data['username']).exists():
#                 return render(request, template, {
#                     'form': form,
#                     'error_message': 'Username already exists.'
#                 })
#             elif User.objects.filter(email=form.cleaned_data['email']).exists():
#                 return render(request, template, {
#                     'form': form,
#                     'error_message': 'Email already exists.'
#                 })
#             elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
#                 return render(request, template, {
#                     'form': form,
#                     'error_message': 'Passwords do not match.'
#                 })
#             else:
#                 # Create the user:
#                 user = User.objects.create_user(
#                     form.cleaned_data['username'],
#                     form.cleaned_data['email'],
#                     form.cleaned_data['password']
#                 )
#                 user.first_name = form.cleaned_data['first_name']
#                 user.last_name = form.cleaned_data['last_name']
#                 user.phone_number = form.cleaned_data['phone_number']
#                 user.save()

#                 # Login the user
#                 login(request, user)

#                 # redirect to accounts page:
#                 return HttpResponseRedirect('/mymodule/account')

#    # No post data availabe, let's just show the page.
#         else:
#             form = RegisterForm()

#     else:
#         return render(request, 'App/LoginForm.html')


def LoginForm(request):
    if request.method == 'POST':
       role = request.POST.get("role")
       username = request.POST.get("username")
       password = request.POST.get("password")
       user = authenticate(request, username=username, password=password)
       if user :
           if role=="User" and user.groups.filter(name="User").exists():
             dj_login(request,user)
             return redirect('/')
             
           elif(role=="Admin" and user.groups.filter(name="Admin").exists()):
               dj_login(request,user)
               return redirect('/Admin/')

       else:
           messages.info(request,'Invalid username and password!')
           return redirect('login')
    
    param={}
    return render(request, 'App/LoginForm.html',param)



@login_required(login_url='/login')
def Admin(request):
    
    crimes=ComplaintRegister.objects.all()
    return render(request,"App/Admin.html",{"crimes":crimes})


def logout(request):
    dj_logout(request)
    return redirect('login')