from django.shortcuts import render
from django.http import HttpResponse

author = {
    "Имя": "Иван",
    "Отчество": "Петрович",
    "Фамилия": "Иванов",
    "телефон": "8-865-234-12-23",
    "e-mail": "vasia@mail.ru",
}

def about(request):
    text = f"""
    <p>Имя: <b>{author["Имя"]}</b></p>
    <p>Отчество: <b>{author["Отчество"]}</b></p>
    <p>Фамилия: <b>{author["Фамилия"]}</b></hp>
    <p>телефон: <b>{author["телефон"]}</b></p>
    <hp>e-mail: <b>{author["e-mail"]}</b></p>
    """
    return HttpResponse(text)

def home(request):
    text = """
    <h1>"Изучаем Django"</h1>
    <strong>Автор</strong>:<i>Иванов И.П.</i>
    """
    return HttpResponse(text)

# Create your views here.
