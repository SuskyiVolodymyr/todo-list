from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from app.models import Task


def index(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.prefetch_related("tag")
    context = {
        "tasks": tasks
    }
    return render(request, "app/index.html", context)


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
