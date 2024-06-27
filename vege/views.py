from django.shortcuts import render,redirect
from vege.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login")
# Create your views here.
def recipies(request):
    if request.method=='POST':
        data=request.POST
        recipe_image=request.FILES.get('recipe_image')
        recipe_name=data.get('recipe_name')
        recipe_description=data.get('recipe_description')
        
        Recepie.objects.create(
            
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image
        )
    
        return redirect("/recipie/")
    queryset=Recepie.objects.all()
    if request.GET.get('search'):
        queryset=queryset.filter(recipe_name__icontains=request.GET.get('search'))
    context={'Recipies':queryset}


    return render(request,"recipiee.html",context)
@login_required(login_url="/login")
def update_recepie(request,id):
    queryset=Recepie.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        recipe_image=request.FILES.get('recipe_image')
        recipe_name=data.get('recipe_name')
        recipe_description=data.get('recipe_description')

        queryset.recipe_description=recipe_description
        queryset.recipe_name=recipe_name
        if recipe_image:
            queryset.recipe_image=recipe_image
        queryset.save()
        return redirect("/recipie/")



    context={'recipies':queryset}
    return render(request,"update.html",context)
@login_required(login_url="/login")
def delete_recepie(request,id):
    queryset=Recepie.objects.get(id=id)
    queryset.delete()
    return redirect("/recipie/")

def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,"invalid username")
            return redirect("/login/")
        
        user=authenticate(username=username,password=password)

        if user is None:
            messages.error(request,"invalid password")
            return redirect("/login/")
        else:
            login(request,user)
            return redirect("/recipie/")

    return render(request,"login.html")

def logout_page(request):
    logout(request)
    return redirect("/login/")

def register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "name already exists")
            return redirect("/register/")
        if username and password:
            user=User.objects.create(username=username)
            user.set_password(password)
            user.save()
            messages.info(request, "account created successfully")
            return redirect("/register/")
        
    return render(request,"register.html")