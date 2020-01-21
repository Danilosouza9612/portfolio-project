from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog'),
    path("<int:id_post>", views.detail, name='detail')
]