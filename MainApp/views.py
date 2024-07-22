from django.shortcuts import render
from django.http import HttpResponse

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]

def home(request):
    text = """
    <h1>"Изучаем Django"</h1>
    <strong>Автор</strong>:<i>Иванов И.П.</i>
    """
    return HttpResponse(text)

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
    <p>e-mail: <b>{author["e-mail"]}</b></p>
    """
    return HttpResponse(text)

def product_n(request, id):
    
    match id:
        case 1: m = 0
        case 2: m = 1
        case 5: m = 2
        case 7: m = 3
        case 8: m = 4
        case _: m = -1
    
    if m != -1:
        text = f"""
        {items[m]["id"]}. {items[m]["name"]}, количество: {items[m]["quantity"]}
        """
    else:
        text = f"Товар с id={id} не найден"
    
    return HttpResponse(text)
    
def products(request):
    text = ''
    for i in range(5):
       text += f"""
        <p>{items[i]["id"]}. <a href="{items[i]["id"]}.html">{items[i]["name"]}</a>, количество: {items[i]["quantity"]}
        """
    
    return HttpResponse(text)

def page_1(request):
    text = f"""
        <h1>{items[0]["id"]}. {items[0]["name"]}, количество: {items[0]["quantity"]}</h1>
        <h2><a href="items">Назад </a></h2>
        """
    return HttpResponse(text)

def page_2(request):
    text = f"""
        <h1>{items[1]["id"]}. {items[1]["name"]}, количество: {items[1]["quantity"]}</h1>
        <h2><a href="items">Назад </a></h2>
        """
    return HttpResponse(text)

def page_5(request):
    text = f"""
        <h1>{items[2]["id"]}. {items[2]["name"]}, количество: {items[2]["quantity"]}</h1>
        <h2><a href="items">Назад </a></h2>
        """
    return HttpResponse(text)

def page_7(request):
    text = f"""
        <h1>{items[3]["id"]}. {items[3]["name"]}, количество: {items[3]["quantity"]}</h1>
        <h2><a href="items">Назад </a></h2>
        """
    return HttpResponse(text)

def page_8(request):
    text = f"""
        <h1>{items[4]["id"]}. {items[4]["name"]}, количество: {items[4]["quantity"]}</h1>
        <h2><a href="items">Назад </a></h2>
        """
    return HttpResponse(text)