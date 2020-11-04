from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.conf import settings
from .models import thumbnail
from .form import input_form, CreateUserForm, new_movie_form
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from .filter import Moviefilter

def handle_uploaded_file(f):   
    with open('media/images/'+f.name, 'wb+') as destination:   
        for chunk in f.chunks(): 
            destination.write(chunk)   

@login_required(login_url='login')
def create_form(request, req_id, *args, **kwargs):
    ele = thumbnail.objects.get(id = req_id)
    user = request.user
    if not user.is_authenticated:
         return redirect(settings.LOGIN_URL)
 
    form = input_form(request.POST or None)
   # print(form)
    next_url = request.POST.get('next') or None
    if form.is_valid():
        if ele.avg_rate != 0:
            ele.avg_rate = (int(ele.avg_rate)  + form.cleaned_data['rate'])/2
        else:
            ele.avg_rate = form.cleaned_data['rate']
        ele.rated_user = request.user.id
        ele.save()
        if next_url != None:
            return redirect(next_url)
        form = input_form()
    return render(request, "components/form.html", context={"form":form})

def home(request, *args, **kargs):
    #print(request.user)
    #return HttpResponse("<h1>Started</h1>")
    a = thumbnail.objects.all()
    home_page = [{"id" : x.id , "title": x.title, "image":x.image.url, "genre":x.genre, "language":x.language, "content" : x.content , "avg_rate" : x.avg_rate} for x in a]

    myfilter  = Moviefilter(request.GET , queryset = a or None)
    home_page = myfilter.qs
    if myfilter == None:
         messages.info(request,'Not Found')
    else:
        return render(request, "pages/home_temp.html",context={'home_page':home_page, 'myfilter':myfilter})

def register_form(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form':form}
    return render(request, "register.html", context)

def login_form(request):
    user = request.user

    if user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request,'Incorrect Id or Password')
                return redirect('login')

    context = {}
    return render(request, "login.html", context)

def logOut(request):
    logout(request)
    return redirect('home')

def filter_data(request):
    return render(request, 'basic-88/index.html')

def edit_delete(request, req_id):
    thumbnail.objects.filter(id = req_id).delete()
    return redirect('home')

def upload(request):
    form = new_movie_form(request.POST, request.FILES)
    #print(form.is_valid())
    if form.is_valid():
     #   print(request.FILES['image'])
        form.save()
        return redirect('home')
    form = new_movie_form()
    return render(request, "components/upload.html", context={'form':form})


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

def thumbnail_list(request, *args, **kargs):
    a = thumbnail.objects.all()
    thumbnail_l = [{"id" : x.id , "title": x.title, "image":x.image.url, "genre":x.genre, "language":x.language, "content" : x.content , "avg_rate" : x.avg_rate} for x in a]
    data = {
        "op":thumbnail_l
    }
    return JsonResponse(data)


