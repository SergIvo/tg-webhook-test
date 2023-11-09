import hashlib

from django.contrib import admin

from .models import WebhookResponse, RegisteredBot


@admin.register(WebhookResponse)
class WebhookResponseAdmin(admin.ModelAdmin):
    readonly_fields = ['recieved_at']
    fields = ['response_content']


@admin.register(RegisteredBot)
class RegisteredBotAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'API_token', 'secret_token_hash']

    def save_model(self, request, obj, form, change):
        if form.initial.get('secret_token_hash') != form.data.get('secret_token_hash'):
            hashed_token = hashlib.sha256(obj.secret_token_hash.encode())
            obj.secret_token_hash = hashed_token.hexdigest()

        super().save_model(request, obj, form, change)

