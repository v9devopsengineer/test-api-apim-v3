from django.shortcuts import render

# Create your views here.
# api/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# This will handle GET, POST, and PUT requests
@csrf_exempt
def api_view(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'GET request received!'})
    elif request.method == 'POST':
        data = json.loads(request.body)
        return JsonResponse({'message': 'POST request received!', 'data': data})
    elif request.method == 'PUT':
        data = json.loads(request.body)
        return JsonResponse({'message': 'PUT request received!', 'data': data})
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)
