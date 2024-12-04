from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import *

# Create your views here.
def platform(request):
    title = 'Games'
    my_buyers = Buyer.objects.all()
    context = {
        'title': title,
        'my_buyers': my_buyers,
    }
    return render(request, 'fourth_task/platform.html', context)

def games(request):
    games = Game.objects.all()
    return render(request, 'fourth_task/games.html', context={'games': games})

def cart(request):
    title = 'Cart'
    context = {
        'title': title,
    }
    return render(request, 'fourth_task/cart.html', context)



# Create your views here.
users = ['user1', 'user2', 'user3']

def sign_up_by_html(request):
        info = {}
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            repeat_password = request.POST.get('repeat_password')
            age = int(request.POST.get('age'))

            buyers = Buyer.objects.values_list('name', flat=True)

            if username in buyers:
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                Buyer.objects.create(name=username, age=age, balance=1000)
                info['message'] = f'Приветствуем, {username}!'

        return render(request, 'fifth_task/registration_page.html', info)
def sign_up_by_django(request):
    info = {}
    form = UserRegister(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            buyers = Buyer.objects.values_list('name', flat=True)

            if username in buyers:
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                Buyer.objects.create(name=username, age=age, balance=1000)
                info['message'] = f'Приветствуем, {username}!'

        info['form'] = form

    return render(request, 'fifth_task/registration_page.html', info)