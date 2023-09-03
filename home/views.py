from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contact ,Order
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        messages.success(request, "Alert!!! Please Log-in. ")
        return redirect('/Login') 
    return render(request, 'index.html')
    # return HttpResponse("You're seeing Home Page. Welcome To Home Page :)")
def about(request):
    return render(request, 'about.html')
def service(request):
    return render(request, 'service.html')

#  ----- Contact Form Section ----

def contact(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        number= request.POST.get('number')
        desc= request.POST.get('desc')
        cont = Contact(name=name, email=email, number=number,desc=desc, date=datetime.today())
        cont.save()
        messages.success(request, "Message sended! See you Shortly :)")
    return render(request, 'contact.html')

# ----- Login And Logut Section

def LoginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
               login(request,user)
               return redirect("/")
        else:
               return render(request,'Login.html')

    return render(request, 'Login.html')

def LogoutUser(request):
    logout(request)
    return redirect('/Login')
def Recipes(request): 
    if request.user.is_anonymous:
        messages.success(request, "Alert!!! Log-in Required to view This")
        return redirect('/Login')   
    return render(request,'Recipes.html')

# ----- Order Section

def order(request):
    if request.method == "POST":
        name= request.POST.get('name')
        number= request.POST.get('number')
        number1= request.POST.get('number1')
        total_bill= request.POST.get('total_bill')
        Onion_pizza= request.POST.get('Onion_pizza')
        Sweet_Corn_pizza= request.POST.get('Sweet_Corn_pizza')
        Address= request.POST.get('Address')
        cont = Order(name=name, number=number,number1=number1,Sweet_Corn_pizza=Sweet_Corn_pizza,total_bill=total_bill,Onion_pizza=Onion_pizza,Address=Address, date=datetime.today())
        cont.save()
        messages.success(request, " Order Recieved !!! It Will Take 30 - 40 Mints TO Deliver :)")
    return render(request, 'order.html')
