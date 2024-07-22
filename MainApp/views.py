from django.shortcuts import render
from MainApp import views

def home(request):
    text = """
    <h1>"Изучаем django<h1>
    <strong>Автор</strong>: <i>Ivanov A.A.</i>
    """
    return HttpResponse(text)
# Create your views here.
