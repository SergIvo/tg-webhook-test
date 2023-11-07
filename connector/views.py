from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import WebhookResponse


def redirect_from_index(request):
    return redirect('show_request_data')


@csrf_exempt
def show_request_data(request):
    if request.method == 'POST':
        request_data = dict(request.POST.items())
    elif request.method == 'GET':
        request_data = dict(request.GET.items())
    if request_data:
        new_entry = WebhookResponse.objects.create(response_content=request_data)
    return JsonResponse(request_data)
    
