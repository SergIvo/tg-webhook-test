import json
import hashlib

import httpx
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import WebhookResponse, RegisteredBot


def redirect_from_index(request):
    return redirect('show_request_data')


@csrf_exempt
def show_request_data(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
    elif request.method == 'GET':
        request_data = dict(request.GET.items())
    if request_data:
        new_entry = WebhookResponse.objects.create(response_content=request_data)
    request_data['headers'] = dict(request.headers)
    if request_data['headers'].get('X-Telegram-Bot-Api-Secret-Token'):
        hashed_token = hashlib.sha256(
            request_data['headers'].get('X-Telegram-Bot-Api-Secret-Token').encode()
        )
        bot = RegisteredBot.objects.get(secret_token_hash=hashed_token.hexdigest())
        chat_id = request_data['message']['chat'].get('id')
        message_text = request_data['message'].get('text')
        
        sent_message = httpx.get(
            f'https://api.telegram.org/bot{bot.API_token}/sendMessage', 
            params={'chat_id': chat_id, 'text': f'Вы написали: {message_text}'}
    )
    return JsonResponse(request_data)
    
