from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    text = """
    Имя: <b>Иван</b>
    Отчество: <b>Петрович</b>
    Фамилия: <b>Иванов</b>
    телефон: <b>8-865-234-12-23</b>
    e-mail: <b>vasia@mail.ru</b>
    """
    return HttpResponse(text)
# Create your views here.
