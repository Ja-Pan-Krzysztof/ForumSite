from django.shortcuts import render


def index(requests):
    return render(requests, 'home.html', context={'title': 'home page'})
