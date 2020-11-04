from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.conf import settings
from .models import thumbnail
from .form import input_form, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def thumbnail_list(request, *args, **kargs):
    a = thumbnail.objects.all()
    thumbnail_l = [{"id" : x.id , "title": x.title, "image":x.image.url, "genre":x.genre, "language":x.language, "content" : x.content , "avg_rate" : x.avg_rate} for x in a]
    data = {
        "op":thumbnail_l
    }
    return JsonResponse(data)

@login_required(login_url='login')
def create_form(request, req_id, *args, **kwargs):
    user = request.user
    if not user.is_authenticated:
         return redirect(settings.LOGIN_URL)
    form = input_form(request.POST or None)
    ele = thumbnail.objects.get(id = req_id)
    next_url = request.POST.get('next') or None
    if form.is_valid():
        if ele.avg_rate != None:
            ele.avg_rate = (int(ele.avg_rate)  + form.cleaned_data['rate'])/2
        else:
            ele.avg_rate = form.cleaned_data['rate']
        ele.save()
        if next_url != None:
            return redirect(next_url)
        form = input_form()
    return render(request, "components/form.html", context={"form":form})

def home(request, *args, **kargs):
    print(request.user)
    #return HttpResponse("<h1>Started</h1>")
    return render(request, "pages/home.html",context={})


def register_form(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form':form}
    return render(request, "register.html", context)

def login_form(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,'Incorrect Id or Password')
            return redirect('login')

    context = {}
    return render(request, "login.html", context)

def logOut(request):
    logout(request)
    return redirect('login')

def home_dyn(request, req_id, *args, **kargs):
    data={
        "id":req_id,
    }
    status = 200
    try:
        a = thumbnail.objects.get(id = req_id)
        data['content'] = a.content   
    except:
        data['message'] = "Not Found"
        status = 404
    return JsonResponse(data, status = status) 