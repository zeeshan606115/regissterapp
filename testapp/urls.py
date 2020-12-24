from django.urls import path
from testapp import views

urlpatterns = [
    path('register/', views.register, name = "register"),
    path('', views.index, name = "index"),
    path('login/', views.user_login, name = "login"),
    path('logout/', views.logout, name = "logout"),

]