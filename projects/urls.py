from django.urls import path
from projects import views

app_name = "projects"

urlpatterns = [
    path('', views.index, name="projects"),
    path('<str:pk>', views.project_detail, name="project-detail"),
]