from django.urls import path
from . import views

urlpatterns = [
    path('<str:day>/', views.redirect_to_weekday, name='redirect_to_weekday'),
]