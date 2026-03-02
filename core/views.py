from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

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

    def get_initial(self):
        initial = super().get_initial()
        project_id = self.request.GET.get("project")
        if project_id:
            initial["project"] = project_id
        return initial


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "core/task_form.html"
    fields = ["project", "title", "description", "assigned_to", "tags", "status"]
    success_url = reverse_lazy("task_list")


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "core/task_confirm_delete.html"
    success_url = reverse_lazy("task_list")

class ProjectListView(ListView):
    model = Project
    template_name = "core/project_list.html"
    context_object_name = "projects"
    ordering = ["-created_at"]


class ProjectDetailView(DetailView):
    model = Project
    template_name = "core/project_detail.html"
    context_object_name = "project"


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "core/project_form.html"
    fields = ["name"]
    success_url = reverse_lazy("project_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = "core/project_form.html"
    fields = ["name"]
    success_url = reverse_lazy("project_list")


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = "core/project_confirm_delete.html"
    success_url = reverse_lazy("project_list")