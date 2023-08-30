from django.urls import path
from todos.views import (
    todo_list_list,
    todo_list_detail,
    todo_list_create,
    todo_list_update,
    todo_list_delete,
)


urlpatterns = [
    path("", todo_list_list, name="todo_list_list"),
    path("<int:id>/", todo_list_detail, name="todo_list_detail"),
    path("create/", todo_list_create, name="todo_list_create"),
    path("<int:id>/edit/", todo_list_update, name="todo_list_update"),
    path("<int:id>/delete/", todo_list_delete, name="todo_list_delete"),
]
