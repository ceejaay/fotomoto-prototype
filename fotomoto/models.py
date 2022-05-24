from django.db import models
import requests

class Images(models.Model):
    url = models.CharField(max_length=256)
    for_sale = models.BooleanField()

