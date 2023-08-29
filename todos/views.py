from django.shortcuts import render, get_object_or_404
from todos.models import TodoList


def todo_list_list(request):
    todo_list = get_object_or_404(TodoList)
    context = {
        "todo_list": todo_list,
    }
    return render(request, "todos/list.html", context)
