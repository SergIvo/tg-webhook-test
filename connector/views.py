from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def show_request_data(request):
    if request.method == 'POST':
        request_data = dict(request.POST.items())
    elif request.method == 'GET':
        request_data = dict(request.GET.items())
    return JsonResponse(request_data)
    
