from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    text = """
    <p>Имя: <b>Иван</b></p>
    <p>Отчество: <b>Петрович</b></p>
    <p>Фамилия: <b>Иванов</b></hp>
    <p>телефон: <b>8-865-234-12-23</b></p>
    <hp>e-mail: <b>vasia@mail.ru</b></p>
    """
    return HttpResponse(text)
# Create your views here.
