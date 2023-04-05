from django.shortcuts import render
from .models import Artist
from django.http import JsonResponse

def get_data(request):
    artist_data = Artist.objects.all()
    return JsonResponse(artist_data)
