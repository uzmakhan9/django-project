from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index (request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        return render (request, 'index.html')
    context = {
        "variable1":"this is sent by variable 1",
        "variable2":"this is sent by variable 2"
    }
    return render(request,'index.html', context)
    # return HttpResponse("this is homepage")

def about (request):
    return render(request,'about.html')
    # return HttpResponse("this is about page")

def services (request):
    return render(request,'services.html')
    # return HttpResponse("this is services page")

def contact (request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact=Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your details has been sent!')
    return render(request,'contact.html')
    # return HttpResponse("this is contact page")

def loginUser(request):
    
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        # check if user has entered correct credentials
        user = authenticate(request,username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            messages.success(request, "successfully logged in")
            return render(request,'index.html')             
        else:
            # No backend authenticated the credentials
            messages.error(request, "Invalid credentials. Please try again.")
            return redirect("/login")
    
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")
