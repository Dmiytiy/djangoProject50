# from django.http import HttpResponse, HttpResponseNotFound
# # Create your views here.
#
# def get_week(request, week):
#     if week == 'monday':
#         return HttpResponse('понедельник')
#     elif week == 'tuesday':
#         return HttpResponse('вторник')
#     elif week == 'wensday':
#         return HttpResponse('среда ')
#     else:
#         return HttpResponseNotFound(f'неизвестный знак зодиака {week}')

from django.shortcuts import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

weekday_mapping = {
        '1': 'monday',
        '2': 'tuesday',
        '3': 'wednesday',
        '4': 'thursday',
        '5': 'friday',
        '6': 'saturday',
        '7': 'sunday',
}

def redirect_to_weekday(request, day):
    if day not in weekday_mapping:
        return HttpResponseNotFound(f"Неверный порядок чисел - {day}")
    name_week = weekday_mapping[day]
    redirect_url = reverse('redirect_to_weekday', args=(name_week,))
    return HttpResponseRedirect(redirect_url)