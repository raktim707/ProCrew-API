from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *

# Create your views here.

@csrf_exempt
def webhook(request):
	print("The body is: ", request.body)
	return HttpResponse(request.body)