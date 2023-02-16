from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('register', views.registerUser, name="register"),

    path('account', views.userAccount, name="account"),
    path('edit-account', views.editAccount, name="edit-account"),

    path('', views.profiles, name="profiles"),
    path('user/<str:pk>', views.profile_detail, name="profile-detail"),
]
