from django.shortcuts import render
from django.http import HttpResponse
import json

def index(request):
# should access Model objects and use Templates to prepare responses
    return HttpResponse(json.dumps({"Message": "Hello World"}))
# Create your views here.
