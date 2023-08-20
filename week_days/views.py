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
from django.shortcuts import render, reverse
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

def site_weekday(request, day):
    description_week = weekday_mapping.get(day)
    data_week = {
        'year_born': 1992,
        'city_born': 'chelyabisk',
        'movie_name': 'Zhara'
    }

    return render(request, 'week_days/greeting.html', context={'data_week': data_week})


def get_guinness_world_records(request):
    records = {
        'power_man': "Narve Laert",
        'bar_name': "Bobs BBQ",
        'count_needle': 1888,
    }
    return render(request, 'week_days/guinnesworldrecords.html', context=records)