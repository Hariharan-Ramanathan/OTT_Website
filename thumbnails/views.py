from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from .models import thumbnail
from .form import input_form

def thumbnail_list(request, *args, **kargs):
    a = thumbnail.objects.all()
    thumbnail_l = [{"id" : x.id , "title" : x.title , "content" : x.content, "genre" : x.genre, "likes" : 12} for x in a]
    data = {
        "op":thumbnail_l
    }
    return JsonResponse(data)

def create_form(request, *args, **kwargs):
    form = input_form(request.POST or None)
    next_url = request.POST.get('next') or None
    if form.is_valid():
        obj = form.save(commit = False)
        obj.save()
        if next_url != None:
            return redirect(next_url)
        form = input_form()
    return render(request, "components/form.html", context={"form":form})

def home(request, *args, **kargs):
    print(request.user)
    #return HttpResponse("<h1>Started</h1>")
    return render(request, "pages/home.html",context={})




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