from django.shortcuts import render
from django.http.response import JsonResponse
from tasks import process_url
from celery.result import AsyncResult


def get_manga(request):
    if request.method == 'GET':
        url = request.GET.get('url', None)
        if url:
            try:
                task = process_url.apply_async((url,))
                return JsonResponse({'message': f'Your task {task.id} was created successfully. '
                                                f'You can use the give id to get your manga when it`s ready',
                                     'task': {task.id}}, status=200)
            except Exception as expt:
                return JsonResponse({'error': f'An unexpected error occurred when processing the given url {url}.\n'
                                              f'Exception: {expt}'}, status=400)
        task_id = request.GET.get('task', None)
        if task_id:
            try:
                result = AsyncResult(task_id)
                return JsonResponse({'message': f'Your task {task_id} status is {result.state}.',
                                    'status': result.state}, status=200)
            except Exception as expt:
                return JsonResponse({'error': f'An unexpected error occurred when processing '
                                              f'the given task id {task_id}.\n Exception: {expt}'}, status=400)
