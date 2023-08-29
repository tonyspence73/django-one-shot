from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList
from todos.forms import TodoForm


def todo_list_list(request):
    todo_list = TodoList.objects.all()
    context = {
        "todo_list": todo_list,
    }
    return render(request, "todos/list.html", context)


def todo_list_detail(request, id):
    todolist = get_object_or_404(TodoList, id=id)
    return render(request, "todos/detail.html", {"todolist": todolist})


def todo_list_create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            list = form.save()
            return redirect("todo_list_detail", id=list.id)
    else:
        form = TodoForm()

    context = {
        "form": form,
    }

    return render(request, "todos/create.html", context)
