from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature 

# Create your views here.
def index (request):
   features = Feature.objects.all()
   return render(request, 'index.html', {'features' : features})

def register(request):
     if request.method=='POST':
        username = request.POST['un']
        email = request.POST['email']
        passw = request.POST['password']
        rp = request.POST['rpassword']
        
        if passw == rp:
            if User.objects.filter(email=email):
                messages.info(request, 'Email already Used')
                return redirect('register')
               
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already Used')
                return redirect('register')
            
            else:
                user = User.objects.create_user(username=username, email=email, password=passw)
                user.save()
                return redirect('login')
        
        
        else:
            messages.info(request, 'Password not same')
            return redirect('register')   
            
     return render(request, 'register.html')  
 
 
def login(request):
     if request.method=='POST':
        username = request.POST['username']
        # email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(username = username, password = password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')   #loging to the home page
        else:
            messages.info(request, 'Credential Invalied')
            return redirect('login')
     else:   
       return render(request, 'login.html')  
     
     
def logout(request):
       return render(request, 'logout.html')  
         

def counter(request):
    # Safely get the 'text' parameter from the request, defaulting to an empty string if it's not provided
    text = request.POST['text']
    amount_of_words = len(text.split())   
    return render(request, 'counter.html', {'text': text})


