from django.urls import path

from app.views import (
    index,
    TaskCreateView,
    TagCreateView,
    TagListView,
    TagUpdateView,
    TagDeleteView,
    TaskUpdateView,
    TaskDeleteView,
    change_status,
)

urlpatterns = [
    path(
        "",
        index,
        name="index"
    ),
    path(
        "task/create",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "task/<int:pk>/update",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "task/<int:pk>/delete",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "task/<int:pk>/change_status",
        change_status,
        name="task-change-status"
    ),
    path(

        "tags/",
        TagListView.as_view(),
        name="tag-list"
    ),
    path(
        "tag/create",
        TagCreateView.as_view(),
        name="tag-create"
    ),
    path(
        "tag/<int:pk>/update",
        TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tag/<int:pk>/delete",
        TagDeleteView.as_view(),
        name="tag-delete"
    ),
]

app_name = "app"
