from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

zodiac_dict = {
    'Aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'Taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'Gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'Cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'Leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'Virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'Libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'Scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'Sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'Capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    ' Aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'Pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

types = {
    'fire' : ['Aries', 'Leo', 'Sagittarius'],
    'eqrth' : ['Taurus', 'Virgo', 'Capricorn'],
    'air' : ['Gemini', 'Libra', ' Aquarius', ],
    'water': ['Cancer', 'Scorpio', 'Pisces']
}

# def det_info_about_sign_zadiac(request, sign_zodiac):
#     if sign_zodiac == 'leo':
#         return HttpResponse('Лев - пятый знак зодиака. СОлнце с 23 июля по 21 августа  ')
#     elif sign_zodiac == 'scorpion':
#         return HttpResponse('Скорпион - восьмой знак зодиака. СОлнце с 24 октября по 21 августа  ')
#     elif sign_zodiac == 'taurus':
#         return HttpResponse('Телец второй знак ')
#     else:
#         return HttpResponseNotFound(f'неизвестный знак зодиака {sign_zodiac}')
def index(request):
    # Получаем список всех знаков зодиака из словаря
    zodiacs = list(zodiac_dict)
    # Инициализируем переменную для сохранения HTML-кода ссылок
    rez = ''
    # Проходимся по каждому знаку зодиака
    for sign in zodiacs:
        # Создаем URL-путь для конкретного знака, используя его имя
        redirect_path = reverse('horoscope-name', args=[sign, ])
        # Добавляем HTML-код ссылки на знак зодиака в переменную rez
        rez += f"<li> <a href='{redirect_path}'>{sign}</a> </li>"
    # Генерируем итоговый HTML-код списка ссылок на знаки зодиака
    response = f"""
    <ol>
        {rez}
    </ol>

    """
    # Возвращаем HTTP-ответ с итоговым HTML-кодом
    return HttpResponse(response)

def det_info_about_sign_zadiac(request, sign_zodiac: str):
    # Получаем описание знака зодиака из словаря
    description = zodiac_dict.get(sign_zodiac, None)
    if description:
        # Возвращаем HTTP-ответ с описанием знака зодиака в виде заголовка
        return HttpResponse(f'<h2> {description}</h2>')
    else:
        # Возвращаем HTTP-ответ с сообщением об ошибке, если знак не найден
        return HttpResponseNotFound(f"неизвестный знак зодиака- {sign_zodiac}")

def det_info_about_sign_zadiac_by_number(request, sign_zodiac: int):
    # Получаем список всех знаков зодиака
    zodiacs = list(zodiac_dict.keys())
    if sign_zodiac > len(zodiacs) or sign_zodiac < 1:
        # Возвращаем HTTP-ответ с сообщением об ошибке, если указан некорректный порядковый номер
        return HttpResponseNotFound(f"Неправильный порядок чисел - {sign_zodiac}")
    # Получаем имя знака зодиака по порядковому номеру
    name_zodiac = zodiacs[sign_zodiac - 1]
    # Создаем URL-путь для знака зодиака по его имени
    redirect_url = reverse('horoscope-name', args=[name_zodiac, ])
    # Выполняем перенаправление на созданный URL-путь
    return HttpResponseRedirect(redirect_url)
def get_signs_by_element(request, element):
    # Преобразуем переданный элемент в нижний регистр
    element = element.lower()
    if element in types:
        # Получаем список знаков зодиака для указанной стихии
        sign_list = types[element]
        sign_links = []
        for sign in sign_list:
            # Создаем URL-путь для знака зодиака по его имени
            redirect_path = reverse('horoscope-name', args=[sign, ])
            # Добавляем HTML-код ссылки на знак зодиака в переменную sign_links
            sign_links.append(f"<li><a href='{redirect_path}'>{sign}</a></li>")
        # Генерируем итоговый HTML-код списка ссылок на знаки зодиака для указанной стихии
        response = f"<ul>{''.join(sign_links)}</ul>"
        # Возвращаем HTTP-ответ с итоговым HTML-кодом
        return HttpResponse(response)
    else:
        # Возвращаем HTTP-ответ с сообщением об ошибке, если указана неправильная стихия
        return HttpResponseNotFound("Неправильная стихия")

def get_info_types(request):
    type_links = []
    for element in types:
        # Создаем URL-путь для списка знаков зодиака по указанной стихии
        redirect_path = reverse('horoscope-signs', args=[element, ])
        # Добавляем HTML-код ссылки на стихию в переменную type_links
        type_links.append(f"<li><a href='{redirect_path}'>{element.capitalize()}</a></li>")
    # Генерируем итоговый HTML-код списка ссылок на стихии
    response = f"<ul>{''.join(type_links)}</ul>"
    # Возвращаем HTTP-ответ с итоговым HTML-кодом
    return HttpResponse(response)

#по веденной дате рассчитать гороскоп
def get_info_by_date(request, month, day):
    return HttpResponse(f'<h2> месяц - {month}, день {day}</h2>')