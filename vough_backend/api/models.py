from django.db import models


class Organization(models.Model):
    login = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255, null=True)
    score = models.IntegerField()
