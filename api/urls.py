from django.urls import path
from api import views


urlpatterns=[
    path('', views.getRoutes),
    path('projects', views.getProjects),
    path('projects/<str:pk>', views.getProject)
]