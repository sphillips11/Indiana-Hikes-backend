from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.HikerCreateView.as_view(), name="register"),
    # path('login/', views.login_view, name="login"),
]
