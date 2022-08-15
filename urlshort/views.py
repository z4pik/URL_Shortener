from django.shortcuts import render
from .models import ShortUrl
from .forms import CreateNewShortURL
from datetime import datetime
import random, string


def home(request):
    return render(request, 'home.html')


def redirectURL(request, url):
    # Ищем созданный short_url
    current_obj = ShortUrl.objects.filter(short_url=url)
    if len(current_obj) == 0:
        # Если не нашли возвращаем - pagenotfound
        return render(request, 'pagenotfound.html')
    context = {
        'obj': current_obj[0]
    }
    return render(request, 'redirect.html', context)


def createShortURL(request):
    if request.method == 'POST':
        # Создаем новую форму
        form = CreateNewShortURL(request.POST)
        if form.is_valid():
            # Получаем настоящию ссылку на сайт
            original_website = form.cleaned_data['original_url']
            # Получаем все символы
            random_chars_list = list(string.ascii_letters)
            # Создаём пустую строку, которая и будет - short_url
            random_chars = ''
            for i in range(6):
                # Наполняем ссылку случайными символами
                random_chars += random.choice(random_chars_list)
            while len(ShortUrl.objects.filter(short_url=random_chars)) != 0:
                for i in range(6):
                    # Наполняем ссылку случайными символами
                    random_chars += random.choice(random_chars_list)
            d = datetime.now()
            s = ShortUrl(
                original_url=original_website,
                short_url=random_chars,
                time_date_created=d
            )
            s.save()
            return render(request, 'urlcreated.html',
                          {'chars': random_chars})

    else:
        form = CreateNewShortURL()
        context = {'form': form}
        return render(request, 'create.html', context)
