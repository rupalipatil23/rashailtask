from django.shortcuts import render, redirect
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def get_id_from_session(request):
    id=request.session['id']
    return id

@login_required()
def homeView(request):
    data=Product.objects.all()
    return render(request, "home.html",{"data":data})

@login_required()
def addView(request):
    if request.method=="POST":
        name=request.POST['name']
        description=request.POST['description']
        price=request.POST['price']
        Product.objects.create(name=name, description=description,price=price)
        return redirect('homeView')
    
    return render(request, "add.html")

@login_required()
def deleteView(request,id):
        Product.objects.filter(id=id).delete()
        return redirect('homeView')
  
@login_required()  
def editView(request,id):
    data= Product.objects.filter(id=id)
    if request.method=="GET":
        return render(request, "edit.html", {"data":data})
    else:
        name=request.POST['name']
        description=request.POST['description']
        price=request.POST['price']
        data.update(name=name, description=description, price=price)
        return redirect('homeView')
        