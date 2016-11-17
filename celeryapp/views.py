from django.shortcuts import render
from django.shortcuts import HttpResponse
from celery import group
from django.views.decorators.csrf import csrf_exempt
from tasks import *

# Create your views here.
def landing_page(request):
    return render(request, 'index.html', {})

def get_reqeust_data(request):
    data = []
    first_url = request.POST["first_url"]
    second_url = request.POST["second_url"]
    third_url = request.POST["third_url"]
    fb_url = request.POST["fb_url"]
    data.append(first_url)
    data.append(second_url)
    data.append(third_url)
    return data, fb_url

@csrf_exempt
def run_async_tasks(request):
    links, fb_profile = get_reqeust_data(request)
    gr = group(retrieve_response.si(links[0]),
               retrieve_response.si(links[1]),
               retrieve_response.si(links[2]),
               retrieve_fb_id_by_profile_url.si(fb_profile))
    res = gr().get()
    response = str(res)
    return HttpResponse(response, content_type="text/html; charset=utf-8")

@csrf_exempt   
def run_sync_tasks(request):
    links, fb_profile = get_reqeust_data(request)
    sync_responses = []
    sync_responses.append(retrieve_response(links[0]))
    sync_responses.append(retrieve_response(links[1]))
    sync_responses.append(retrieve_response(links[2]))
    sync_responses.append(retrieve_fb_id_by_profile_url(fb_profile))
    response = str(sync_responses)
    return HttpResponse(response, content_type="text/html; charset=utf-8")