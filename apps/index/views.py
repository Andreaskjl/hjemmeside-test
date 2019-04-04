from django.shortcuts import render


def home(request):
    context = {'hej': 1}
    return render(request, 'home.html', context)


def about(request):
    context = {'name': 'Andreas'}
    return render(request, 'about.html', context)


def contact(request):
    context = {'hej': 1}
    return render(request, 'contact.html', context)


def news(request):
    context = {'hej': 1}
    return render(request, 'news.html', context)