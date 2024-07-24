from django.urls import path

from app.views import (
    index,
    TaskCreateView,
    TagCreateView,
    TagListView,
    TagUpdateView
)

urlpatterns = [
    path("", index, name="index"),
    path("task/create", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tag/create", TagCreateView.as_view(), name="tag-create"),
    path("tag/<int:pk>/update", TagUpdateView.as_view(), name="tag-update"),

]

app_name = "app"
