from django.shortcuts import render, get_object_or_404
from todos.models import TodoList


def todo_list_list(request):
    todo_list = TodoList.objects.all()
    context = {
        "todo_list": todo_list,
    }
    return render(request, "todos/list.html", context)


def todo_list_detail(request, id):
    todolist = get_object_or_404(TodoList, id=id)
    return render(request, "todos/detail.html", {"todolist": todolist})
