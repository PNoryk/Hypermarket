from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def basket_adding(request):
    return_dictionary = dict()
    session_key = request.session.session_key

    return JsonResponse(return_dictionary)