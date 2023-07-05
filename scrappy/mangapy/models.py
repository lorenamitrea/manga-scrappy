from django.db import models


class Manga(models.Model):
    url = models.CharField(max_length=500)
    name = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True)


class Chapter(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    result = models.FileField()


class Image(models.Model):
    image = models.ImageField()
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    number = models.IntegerField()
