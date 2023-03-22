import os
import pickle
import json
import base64

from PIL import Image

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import F, Count
from django.views import generic
from django.utils import timezone

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from django.http import HttpResponse
from django.template import loader

from .models import Feedback

from django.shortcuts import render

from .forms import FeedbackForm, RecognitionForm

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
WORK_DIR = os.path.join(ROOT_DIR, 'flora')

menu_items = {
    "index": "Главная",
    "houseplants": "Комнатные растения",
    "street": "Уличные растения",
    "bouquets": "Букеты",
    "feedback": "Обратная связь",
    "login": "Личный кабинет",
    "graphics": "Инфографика",
    "gallery": "Галерея",
    "neuron": "Определить растение",
    "graphics": "Графики и Диаграммы"
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


# class FeedbackView(generic.ListView):
#     model = Feedback
#     template_name = 'flora/feedback.html'


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


def graphics(request):
    return render(request, 'flora/graphics.html', global_context)


def gallery(request):
    return render(request, 'flora/gallery.html', global_context)


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


def graphics(request):
    return render(request, 'flora/graphics.html', global_context)
