from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=150)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = (
        ("todo", "To Do"),
        ("doing", "Doing"),
        ("done", "Done"),
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")  # many-to-one ✅
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    assigned_to = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="tasks"
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="tasks")  # many-to-many ✅
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="todo")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title