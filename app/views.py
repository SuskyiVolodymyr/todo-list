from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseRedirect
)
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from app.forms import TaskForm
from app.models import Task, Tag


def index(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.prefetch_related("tags")
    context = {
        "tasks": tasks
    }
    return render(request, "app/index.html", context)


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("app:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("app:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("app:index")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("app:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("app:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("app:tag-list")


def change_status(request: HttpRequest, pk: int) -> HttpResponse:
    task = Task.objects.get(id=pk)
    task.is_done = task.is_done is False
    task.save()
    return HttpResponseRedirect(request.META.get(
            "HTTP_REFERER",
            reverse_lazy("app:index")
        ))
