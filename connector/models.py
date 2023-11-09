from django.db import models


class WebhookResponse(models.Model):
    recieved_at = models.DateTimeField(
        'Date and time when webhook responded',
        auto_now = True
    )
    response_content = models.TextField('Response JSON')

    class Meta:
        verbose_name = 'Webhook response'
        verbose_name_plural = 'Webhook responses'

    def __str__(self):
        return self.recieved_at


class RegisteredBot(models.Model):
    name = models.CharField('Telegram bot name', max_length=50)
    description = models.TextField('Telegram bot description', blank=True, null=True)
    API_token = models.CharField('Telegram bot API token', max_length=50, unique=True)
    secret_token_hash = models.CharField('Bot webhook hashed token', max_length=64, unique=True)

    class Meta:
        verbose_name = 'Registered bot'
        verbose_name_plural = 'Registered bots'

    def __str__(self):
        return self.recieved_at
