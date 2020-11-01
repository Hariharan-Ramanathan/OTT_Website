from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from .models import thumbnail

def home(request, *args, **kargs):
    return HttpResponse("<h1>Started</h1>")

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
    return JsonResponse(data, status = status) #json.dumps content_type='application/json'