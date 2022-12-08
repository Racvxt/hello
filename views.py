from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from shop.models import Destination, Product
from .models import Product
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def index(request):
    return HttpResponse("Hi Rabindra")
def jkl(request):
    return render(request,'shop/jkl.html') 
def hi(request):
    return render(request,'about.html')      
def test(request):
    context={
        "lname":"Rabindra",
        "list_of_name": [
            {
                "name":"Rabindra",
                "age":21,
                "bool":True
            },
            {
                "name":"Kabita",
                "age":24,
                "bool":True

            }
            ],
        

        
    }
    description=Destination()
    description.desc='shop/textfile.txt'

    return render(request,'shop/jkl.html',context)  
def addition(request):
    return render(request,'shop/about.html',{"name":"Rabindra"})    
def format(request):
    value1=int(request.GET["num1"])
    value2=int(request.GET["num2"])
    results=value1+value2
    return render(request,'shop/ghj.html',{'res':results})         
def xello(request):
    dest1=Destination()
    dest1.fname="Rabindra"
    dest1.age=20
    return render(request,'shop/ghj.html',{'dest':dest1})
def vb(request):
    return render(request,'shop/dfg.html')    
def testing(request):
    b=Product.objects.all()
    paarams={'imge':b}
    return render(request,'shop/test.html',paarams)    
def forauth(request):
    if request.method=="POST":
        username1=request.POST.get('username')
        password1=request.POST.get('password')
        user=authenticate(request,username=username1,password=password1)
        print(username1)
        if user is not None:
            login(request,user)
            messages.success(request,"Login Successfull.")
            return redirect("/shop/forauth")
        else:
            messages.info(request,"invalid username and password.")
            return redirect('/shop/forauth')
    else:        
        return render(request,'shop/auth.html')
def pagal(request):
    return HttpResponse("hi babau k xa khabar")

