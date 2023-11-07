from django.db import models


class WebhookResponse(models.Model):
    recieved_at = models.DateTimeField(
        'Date and time when webhook responded',
        auto_now = True
    )
    response_content = models.TextField('Response JSON')
