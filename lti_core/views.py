from pickle import GET
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render

import requests
# Create your views here.


def home(request: HttpRequest) -> JsonResponse:
    open_configuration = request.GET.get('openid_configuration', '')
    registration_token = request.GET.get('registration_token', '')
    if open_configuration:
        r = requests.get(request.GET.get('openid_configuration', ''))
        r = r.json()
        
        print("JSON")
        for k,v in r.items():
            print(f"{k}:{v}")
    return JsonResponse(data={
        'response': 'Ok',
        'status': '200',
    })