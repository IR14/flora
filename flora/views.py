import os
import pickle
import json
import io
import base64

import matplotlib.pyplot as plt
import matplotlib as mpl
import random
import numpy as np

from django.utils import timezone
from django.shortcuts import render

from .models import Feedback
from .forms import FeedbackForm, RecognitionForm

mpl.use('svg')

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
WORK_DIR = os.path.join(ROOT_DIR, 'flora')

menu_items = {
    "index": "Главная",
    "houseplants": "Комнатные растения",
    "street": "Уличные растения",
    "bouquets": "Букеты",
    "feedback": "Обратная связь",
    "login": "Личный кабинет",
    "gallery": "Галерея",

    "shop": "Магазин",
    "article": "Полезные статьи",
    "test": "Интересные факты",
    "animation": "animation",

    "neuron": "Определить растение",
    "graphics": "Графики и Диаграммы",
    "care": "Уход за растениями",
    "neuroart": "Нейронные статьи",
    "calculator": "Необычный калькулятор"
}

flower_species = {
    'buddy rose': 'Гомфрена',
    'lily': 'Лилия',
    'parijat': 'Жасмин ночной',
    'pink lily': 'Лилия розовая',
    'pink rose': 'Роза розовая',
    'red rose': 'Роза обыкновенная',
    'red sadaful': 'Катарантус красный',
    'sunflower': 'Подсолнечник',
    'sunflower mini': 'Подсолнечник карликовый',
    'water flower': 'Лотус',
    'white rose': 'Роза белая',
    'white lily': 'Лилия белая',
    'white sadaful': 'Катарантус белый',
    'winter flower': 'Подснежник',
    'yellow lily': 'Лилия желтая'

}

global_context = {
    "menu_list": menu_items
}

model_path = os.path.join(WORK_DIR, 'model.sav')
model = pickle.load(open(model_path, 'rb'))


def index(request):
    return render(request, 'flora/index.html', global_context)


def neuron(request):
    img_path = os.path.join(WORK_DIR, 'test.jpg')

    if request.method == 'POST':
        form = RecognitionForm(request.POST, request.FILES)
        if form.is_valid():
            img_obj = request.FILES['image']

            with open(img_path, 'wb+') as image_to_write:
                for chunk in img_obj.chunks():
                    image_to_write.write(chunk)

            try:
                prediction = model.predict(img_path).json()['predictions'][0]['class']
                img_class = flower_species[prediction]
            except IndexError:
                img_class = None

            with open(img_path, "rb") as image_to_read:
                image_data = base64.b64encode(image_to_read.read()).decode('utf-8')

            return render(request,
                          'flora/neuron.html',
                          {'form': form} | {'img_class': img_class, 'image': image_data} | global_context)
    else:
        form = RecognitionForm()

    return render(request, 'flora/neuron.html', {'form': form} | global_context)


def houseplants(request):
    return render(request, 'flora/houseplants.html', global_context)


def bouquets(request):
    return render(request, 'flora/bouquets.html', global_context)


def street(request):
    return render(request, 'flora/street.html', global_context)


def test(request):
    return render(request, 'flora/test.html', global_context)


def gallery(request):
    return render(request, 'flora/gallery.html', global_context)


def shop(request):
    return render(request, 'flora/shop.html', global_context)


def article(request):
    return render(request, 'flora/article.html', global_context)


def animation(request):
    return render(request, 'flora/animation.html', global_context)


def care(request):
    return render(request, 'flora/care.html', global_context)


def neuroart(request):
    return render(request, 'flora/neuroart.html', global_context)


def calculator(request):
    return render(request, 'flora/calculator.html', global_context)


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            mail = form.cleaned_data['mail']
            category = form.cleaned_data['category']
            feedback_text = form.cleaned_data['feedback_text']
            pub_date = timezone.now()

            Feedback.objects.create(user=user,
                                    mail=mail,
                                    category=category,
                                    feedback_text=feedback_text,
                                    pub_date=pub_date)

    form = FeedbackForm()
    return render(request, 'flora/feedback.html', {'form': form} | global_context)


def fig_to_base64(fig):
    img = io.BytesIO()
    fig.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)

    return base64.b64encode(img.getvalue())


def graphics(request):
    names = ['Орхидея', 'Фиалка', 'Фикус', 'Антриум',
             'Замиокулькас', 'Гортезия', 'Монстера',
             'Кактус', 'Алоэ', 'Пеларгония']

    values = [1065.0, 170.0, 1000.0, 550.0, 960.0, 620.0, 1660.0, 400.0, 280.0, 470.0]
    # values2 = [0.64, 0.48, 0.48, 0.43, 0.40, 0.36, 0.35, 0.32, 0.31, 0.31]
    n = len(names)

    plt.figure(figsize=(16, 9), dpi=80)
    all_colors = list(plt.cm.colors.cnames.keys())
    random.seed(100)
    c = random.choices(all_colors, k=n)

    plt.bar(names, values, width=0.3, color=c)

    for i, val in enumerate(zip(values, names)):
        plt.text(i, val[0], val[0],
                 horizontalalignment='center',
                 verticalalignment='bottom',
                 fontdict={'fontweight': 500, 'size': 13})

    plt.gca().set_xticklabels(names, rotation=45, horizontalalignment='right', fontdict={'size': 13})

    # X/Y label Settings
    plt.ylabel('Sales (RUB ₽)', fontsize=17)
    plt.yticks(fontsize=13, alpha=.7)
    plt.title("Flowers' prices", fontsize=17)
    plt.grid(axis='y', alpha=.3)

    plt.gca().spines["top"].set_alpha(0.0)
    plt.gca().spines["bottom"].set_alpha(0.5)
    plt.gca().spines["right"].set_alpha(0.0)
    plt.gca().spines["left"].set_alpha(0.5)

    # fig = plt.figure()

    # fig = plt.savefig()
    # imgdata = StringIO()
    # fig.savefig(imgdata, format='svg')
    # imgdata.seek(0)
    # data = imgdata.getvalue()

    # data = fig_to_base64(fig)

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=80)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
    buf.close()

    plt.close()

    return render(request, 'flora/graphics.html', {'graph': image_base64} | global_context)
