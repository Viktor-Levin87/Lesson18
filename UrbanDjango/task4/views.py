from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


def index_platform(request):
    title = 'Главная страница'
    context = {
        'title': title,
    }
    return render(request, 'fourth_task/platform.html', context)


def index_cart(request):
    title = 'Корзина'
    text = 'Извините, ваша корзина пуста'
    text2 = 'Вернуться обратно'
    context = {
        'title': title,
        'text': text,
        'text2': text2,
    }
    return render(request, 'fourth_task/cart.html', context)


def index_games(request):
    title = 'Магазин'
    text = 'Игры'
    game = ['GTA5', 'CyberPunk 2077', 'Counter-Strike: CS']
    text_but1 = 'Купить'
    text_but2 = 'Вернуться обратно'
    context = {
        'title': title,
        'text': text,
        'game': game,
        'text_but1': text_but1,
        'text_but2': text_but2,
    }
    return render(request, 'fourth_task/games.html', context)
