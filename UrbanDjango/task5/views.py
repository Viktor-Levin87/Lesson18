from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


def chek_user(users, username, password, repeat_password, age):
    if username in users:
        return 'Пользователь уже существует'
    if password != repeat_password:
        return 'Пароли не совпадают'
    if int(age) < 18:
        return 'Вы должны быть старше 18 лет!'
    else:
        return None


def sign_up_by_html(request):
    users = ['user1', 'user2', 'user5']
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        erorr = chek_user(users, username, password, repeat_password, age)
        if erorr:
            info = {'error': erorr}
            return render(request, 'fifth_task/registration_page.html', context=info)
        else:
            return HttpResponse(f'Приветствуем, {username}!')
    return render(request, 'fifth_task/registration_page.html')


def sign_up_by_django(request):
    users = ['user1', 'user2', 'user5']
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            erorr = chek_user(users, username, password, repeat_password, age)
            if erorr:
                info = {'error': erorr}
                return render(request, 'fifth_task/registration_page.html', context=info)
            else:
                return HttpResponse(f'Приветствуем, {username}!')
    else:
        form = UserRegister()
        info = {'form': form}
    return render(request, 'fifth_task/registration_page.html', context=info)
