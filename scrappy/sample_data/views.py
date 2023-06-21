import time

from django.shortcuts import render
from .models import Artist
from django.http import JsonResponse, HttpResponse
from .tasks import wait
from .forms import WaitForm
from django.template import loader
from celery.result import AsyncResult


def get_data(request):
    if request.method == 'GET':
        artist_data = Artist.objects.all()
        return JsonResponse(artist_data)


def wait_for_me(request):
    if request.method == 'POST':
        form = WaitForm(request.POST)
        if form.is_valid():
            task = wait.delay(form.cleaned_data['seconds'])
            return JsonResponse({"task_id": task.id}, status=202)

    else:
        form = WaitForm()

    return render(request, "sample_data/home.html", {"form": form})


def sleep_task(request):
    seconds = request.GET.get('seconds', None)
    if seconds:
        print(seconds)
        task = wait.apply_async((int(seconds),))
        time.sleep(3)
        result = AsyncResult(task.id)
        return JsonResponse({"task_id": task.id, "status": result.state}, status=202)
    return HttpResponse('Give me some time to wait. I.e. /sample/sleep?seconds=10')


def get_task_status(request):
    task = request.GET.get('task', None)
    result = AsyncResult(task)
    return JsonResponse({"status": result.state}, status=202)
