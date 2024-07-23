from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

author = {
    "Имя": "Иван",
    "Отчество": "Петрович",
    "Фамилия": "Иванов",
    "телефон": "8-923-600-01-02",
    "email": "vasya@mail.ru",
}


items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]


def home(request):
    context = {
        "name": "Петров Иван Николаевич",
        "email": "my_email@mail.ru"
    }
    #text = """
    #<h1>"Изучаем django"</h1>
    #<strong>Автор</strong>: <i>Иванов И.П.</i>    
    #"""
    #return HttpResponse(text)
    return render(request, "index.html", context)


def about(request):
    text = f"""
    Имя: <b>{author["Имя"]}</b><br>
    Отчество: <b>{author["Отчество"]}</b><br>
    Фамилия: <b>{author["Фамилия"]}</b><br>
    телефон: <b>{author["телефон"]}</b><br>
    email: <b>{author["email"]}</b><br>
    """
    return HttpResponse(text)


def get_item(request, item_id):
    """ По указанному id возвращаем имя и кол-во элемента """
    for item in items:
        if item['id'] == item_id:
            context = {"id": item['id'], "name": item['name'] , "quantity": item['quantity']}
                      
            #result = f"""
            #<h2> Имя: {item["name"]} </h2>
            #<p> Количество: {item["quantity"]} </p>
            #<p> <a href="/items"> Назад к списку товаров </a></p>
            #"""
            return render(request, "item.html", context)
    return HttpResponseNotFound(f"Item with id={item_id} not found.")


def get_items(request):
    context = {
        "items": items
    }

    
    #result = "<h1>Список товаров</h1><ol>"
    #for item in items:
    #    result += f"""<li> <a href="/item/{item['id']}"> {item['name']}</li> """
    #result += "</ol>"
    return render(request, "items.html", context)
    #return HttpResponse(result)