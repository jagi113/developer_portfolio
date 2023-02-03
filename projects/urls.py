from django.urls import path
from projects import views

app_name = "projects"

urlpatterns = [
    path('', views.index, name="projects"),
    path('project/<str:pk>', views.project_detail, name="project-detail"),
    path('create-project', views.create_project, name="create-project"),
    path('update-project/<str:pk>', views.update_project, name="update-project"),
    path('delete-project/<str:pk>', views.delete_project, name="delete-project")
]