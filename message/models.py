from django.db import models

class Message(models.Model):
    author = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    date = models.DateTimeField(default=None, blank=True, null=True)
    likes = models.IntegerField(default=0)
    image = models.CharField(max_length=1000, blank=True)