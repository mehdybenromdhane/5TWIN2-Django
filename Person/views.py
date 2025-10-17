from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth import authenticate,login

from django.contrib import messages


from .forms import UserRegistration
def login_user(request):
    
    
    if request.method=="POST":
        username= request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username , password=password)
    
        if user:
            login(request,user)
            return redirect('listEvents')
        
        else:
            messages.info(request, "Username or password incorrect")
    
    
    return render(request,'person/login.html',{})


def register(request):
    
    if request.user.is_authenticated:
        
        return redirect('listEvents')
    
    
    form =UserRegistration()
    if request.method=='POST':
         form =UserRegistration(request.POST)
         
         if form.is_valid():
             
             
             user =form.save()
             
             login(request,user)
              
             return redirect('listEvents')
         
         else:
             
             for error in list(form.errors.values()):
                 print(request,error)
         
    else: 
        form =UserRegistration()

    
    
    return render(request , 'person/register.html', {'form':form} )