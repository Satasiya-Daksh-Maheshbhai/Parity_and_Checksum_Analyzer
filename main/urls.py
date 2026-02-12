from django.urls import path
from . import views

urlpatterns = [
    path('error/', views.error_detection, name='error_detection'),
]
