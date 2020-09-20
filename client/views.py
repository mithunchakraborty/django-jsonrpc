import json
from django.shortcuts import render
from core.views import base_view
from django.http import JsonResponse
from core.api_services import auth_check
from django.conf import settings


@base_view
def index(request):
    response = auth_check(
        hostname='https://slb.medv.ru/api/v2/',
        certificate_str=settings.API_CERTIFICATE,
        key_str=settings.API_KEY
    )
        
    return render(
        request,
        'client/index.html',
        {
            'response': response
        }
    )

