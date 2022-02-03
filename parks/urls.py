from django.urls import path
from . import views

urlpatterns = [
    path('', views.ParkListView.as_view(), name='parks-list'),
    path('<slug:slug>/', views.ParkDetailView.as_view(), name='park-details'),
]