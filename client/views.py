import json
from django.shortcuts import render
from core.views import base_view
from django.http import JsonResponse
from .services import authentication_check


@base_view
def index(request):
    return JsonResponse({'success': authentication_check()}) 

