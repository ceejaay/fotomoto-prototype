from django.db import models

class Images(models.Model):
    url = models.CharField(max_length=256)
    for_sale = models.BooleanField()
