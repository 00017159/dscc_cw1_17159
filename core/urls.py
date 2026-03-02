from django.urls import path
from .views import ProjectListView
from .views import (
    ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView,
)
from .views import (
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
)

urlpatterns = [
    path("tasks/", TaskListView.as_view(), name="task_list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("tasks/create/", TaskCreateView.as_view(), name="task_create"),
    path("tasks/<int:pk>/edit/", TaskUpdateView.as_view(), name="task_update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
    path("projects/", ProjectListView.as_view(), name="project_list"),
    path("projects/", ProjectListView.as_view(), name="project_list"),
    path("projects/create/", ProjectCreateView.as_view(), name="project_create"),
    path("projects/<int:pk>/", ProjectDetailView.as_view(), name="project_detail"),
    path("projects/<int:pk>/edit/", ProjectUpdateView.as_view(), name="project_update"),
    path("projects/<int:pk>/delete/", ProjectDeleteView.as_view(), name="project_delete"),
    
]