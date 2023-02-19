from django.shortcuts import render


def index(request):
    return render(request, "core/index.html")


def blog(request):
    return render(request, "core/blog.html")
