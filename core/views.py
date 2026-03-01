from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Project, Task, Tag


def home(request):
    return render(request, "core/home.html", {
        "project_count": Project.objects.count(),
        "task_count": Task.objects.count(),
        "tag_count": Tag.objects.count(),
        "recent_tasks": Task.objects.order_by("-created_at")[:5],
    })


class TaskListView(ListView):
    model = Task
    template_name = "core/task_list.html"
    context_object_name = "tasks"
    ordering = ["-created_at"]


class TaskDetailView(DetailView):
    model = Task
    template_name = "core/task_detail.html"
    context_object_name = "task"


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "core/task_form.html"
    fields = ["project", "title", "description", "assigned_to", "tags", "status"]
    success_url = reverse_lazy("task_list")


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "core/task_form.html"
    fields = ["project", "title", "description", "assigned_to", "tags", "status"]
    success_url = reverse_lazy("task_list")


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "core/task_confirm_delete.html"
    success_url = reverse_lazy("task_list")