from django.urls import path
from . import views

urlpatterns = [
    path('<int:day>/', views.redirect_to_weekday, name='redirect_to_weekday'),
    path('day/', views.site_weekday, name='site_weekday'),
    path('record/', views.get_guinness_world_records),
]