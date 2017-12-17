from django.shortcuts import render


def home(request):
    return render(request, template_name='web/home.html', context={})


def about(request):
    return render(request, template_name='web/about.html', context={})
