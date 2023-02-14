from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('register', views.registerUser, name="register"),
    
    path('', views.profiles, name="profiles"),
    path('user/<str:pk>', views.profile_detail, name="profile-detail"),
    
    # path('create-project', views.create_project, name="create-project"),
    # path('update-project/<str:pk>', views.update_project, name="update-project"),
    # path('delete-project/<str:pk>', views.delete_project, name="delete-project")
]