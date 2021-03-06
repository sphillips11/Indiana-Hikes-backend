from django.urls import path
from . import views

urlpatterns = [
    path('', views.HikersView.as_view(), name="hikers"),
    path('<int:id>/', views.HikerView.as_view(), name="hiker_info"),
    path('<int:hiker_id>/hikes/', views.HikesView.as_view(), name="hikes"),
    path('<int:hiker_id>/hikes/<int:id>/', views.HikeView.as_view(), name="hike_details"),
    path('<int:hiker_id>/hikes/trails/<int:park_id>/', views.TrailsByParkHikerView.as_view(), name="trails_by_park_hiker")
]
