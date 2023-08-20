
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='horoscope-index'),
    path('<int:month>/<int:day>', views.get_info_by_date),#для сложного задания
    path('type/', views.get_info_types, name='horoscope-type'),
    path('type/<str:element>/', views.get_signs_by_element, name='horoscope-signs'),
    path('<int:sign_zodiac>/', views.det_info_about_sign_zadiac_by_number),
    path('<str:sign_zodiac>/', views.det_info_about_sign_zadiac, name = 'horoscope-name'),
]

