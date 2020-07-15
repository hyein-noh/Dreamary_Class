from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('introduce/', views.introduce, name = "introduce"),
    path('profile/<int:designer_id>', views.detail, name="detail"),
]