
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


def home(request):
    tasks = Task.objects.all().order_by("-created_at")

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()

        if title:
            Task.objects.create(
                title=title,
                description=description
            )
            return redirect("home")

    return render(request, "tasks/home.html", {"tasks": tasks})


def delete_task(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=task_id)
        task.delete()

    return redirect("home")


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TaskForm(instance=task)

    return render(
        request,
        "tasks/edit_task.html",
        {"form": form, "task": task}
    )


def complete_task(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=task_id)
        task.completed = True
        task.save()

    return redirect("home")
