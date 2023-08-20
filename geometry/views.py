from django.http import HttpResponse
from math import pi
from django.shortcuts import render

def get_rectangle_area(request, width, height):
    area = width * height
    return render(request, 'geometry/rectangle.html')


def get_square_area(request, width):
    area = width ** 2
    #return HttpResponse(f"Площадь квадрата размером {width}x{width} равна {area}")
    return render(request, 'geometry/square.html')
def get_circle_area(request, radius):
    area = pi * (radius ** 2)
    #return HttpResponse(f"Площадь круга радиусом {radius} равна {area:.2f}")
    return render(request, 'geometry/circle.html')
