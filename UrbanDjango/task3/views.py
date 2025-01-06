from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


def index_platform(request):
    title = 'Главная страница'
    text1 = 'Главная'
    text2 = 'Магазин'
    text3 = 'Корзина'
    context = {
        'title': title,
        'text1': text1,
        'text2': text2,
        'text3': text3,
    }
    return render(request,'third_task/platform.html', context)


def index_cart(request):
    title = 'Корзина'
    text = 'Извините, ваша корзина пуста'
    text2 = 'Вернуться обратно'
    context = {
        'title': title,
        'text': text,
        'text2': text2,
    }
    return render(request,'third_task/cart.html', context)


def index_games(request):
    title = 'Магазин'
    text = 'Игры'
    game1 = 'GTA5'
    game2 = 'CyberPunk 2077'
    game3 = 'Counter-Strike: CS'
    text_but1 = 'Купить'
    text_but2 = 'Вернуться обратно'
    context = {
        'title': title,
        'text': text,
        'game1': game1,
        'game2': game2,
        'game3': game3,
        'text_but1': text_but1,
        'text_but2': text_but2,
    }
    return render(request, 'third_task/games.html', context)
