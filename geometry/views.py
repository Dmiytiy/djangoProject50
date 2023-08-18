from django.http import HttpResponse
from math import pi

def get_rectangle_area(request, width, height):
    area = width * height
    return HttpResponse(f"Площадь прямоугольника размером {width}x{height} равна {area}")

def get_square_area(request, width):
    area = width ** 2
    return HttpResponse(f"Площадь квадрата размером {width}x{width} равна {area}")

def get_circle_area(request, radius):
    area = pi * (radius ** 2)
    return HttpResponse(f"Площадь круга радиусом {radius} равна {area:.2f}")