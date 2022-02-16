from django.urls import path
from . import views

urlpatterns = [
    path('', views.ParkListView.as_view(), name='parks-list'),
    path('<slug:slug>/', views.ParkDetailView.as_view(), name='park-details'),
    path('<slug:slug>/map/', views.map_view, name='park-map'),
    path('names/', views.ParkNameView.as_view(), name="park-names"),
    path('trails/<int:park_id>/', views.TrailListView.as_view(), name="trails-by-park"),
]