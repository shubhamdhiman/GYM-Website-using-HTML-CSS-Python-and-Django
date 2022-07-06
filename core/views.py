from django.shortcuts import render
from .forms import CustomerRegistration
from . models import User
from django.http import HttpResponse
def djaboutus(request):
    return render(request,'aboutus.html')

def djcontactus(request):
    return render(request,'contactus.html')

def djhome(request):
    return render(request,'home.html')

def djjoinus(request):
    if request.method =='POST':
        fm = CustomerRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            con = fm.cleaned_data['contact']
            ag = fm.cleaned_data['age']
            gen=fm.cleaned_data['gender']
            reg = User(name=nm, email=em, contact=con,age=ag,gender=gen)
            reg.save()
            return render(request,'thankyou.html',{'name':nm})
            
        
    else:
        fm=CustomerRegistration()
    return render(request,'joinus.html',{'form':fm})

def djservices(request):
    return render(request,'services.html')

def djtrainers(request):
    return render(request,'trainers.html')

