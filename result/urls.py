from django.urls import path
from . import views

urlpatterns = [
    path('save_result/', views.save_result, name='save_result'),
    path('get_all_result/<str:category>/', views.get_all_result, name='get_all_result'),
]