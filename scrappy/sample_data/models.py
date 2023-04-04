from django.db import models


class Artist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=100)
    born_year = models.IntegerField()
    death_year = models.IntegerField(null=True)
