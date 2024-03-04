from django.db import models


# Create your models here.
class Message(models.Model):
    content = models.TextField()
    sender = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
