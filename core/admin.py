from django.contrib import admin
from .models import Project, Task, Tag


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "owner", "created_at")
    search_fields = ("name", "owner__username")
    list_filter = ("created_at",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "project", "status", "assigned_to", "created_at")
    search_fields = ("title", "project__name", "assigned_to__username")
    list_filter = ("status", "project", "tags", "created_at")
    filter_horizontal = ("tags",)
