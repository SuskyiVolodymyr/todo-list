from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "app/index.html")
