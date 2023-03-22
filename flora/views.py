from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import F, Count
from django.views import generic
from django.utils import timezone

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from roboflow import Roboflow
from django.http import HttpResponse
from django.template import loader

from .models import Feedback

from django.shortcuts import render

from .forms import FeedbackForm


menu_items = {
    "index": "Главная",
    "houseplants": "Комнатные растения",
    "street": "Уличные растения",
    "bouquets": "Букеты",
    "feedback": "Обратная связь",
    "login": "Личный кабинет",
    "graphics": "Инфографика",
    "neuron": "Определить растение"
}

global_context = {
    "menu_list": menu_items
}


# class FeedbackView(generic.ListView):
#     model = Feedback
#     template_name = 'flora/feedback.html'


def index(request):
    return render(request, 'flora/index.html', global_context)


def neuron(request):
    rf = Roboflow(api_key="sAA2PirCW9POEOYvCoWV")
    project = rf.workspace("pridch-kirpich-xmkm9").project("flora-cm3ry")
    model = project.version(2).model
    model.predict("flora/images/TestFlower.png", confidence=40, overlap=30).save("prediction3.jpg")
    return render(request, 'flora/neuron.html', global_context)


def houseplants(request):
    return render(request, 'flora/houseplants.html', global_context)


def bouquets(request):
    return render(request, 'flora/bouquets.html', global_context)


def street(request):
    return render(request, 'flora/street.html', global_context)


# def feedback(request):
#     return render(request, 'flora/feedback.html', global_context)


# def registration(request):
#     return render(request, 'flora/registration.html', global_context)


def graphics(request):
    return render(request, 'flora/graphics.html', global_context)


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

# def feedback(request, feedback_id):
#     feedback_item = get_object_or_404(Feedback, pk=feedback_id)
#     try:
#         selected_choice = feedback_item.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Feedback.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'flora/detail.html', {
#             'question': feedback_item,
#             'error_message': "You didn't select a choice.",
#         })


# class FeedbackView(generic.DetailView):
#     model = Feedback
#     template_name = 'flora/feedback.html'

# def sign_up(request):
#     if request.method == 'GET':
#         form = RegisterForm()
#         return render(request, 'users/register.html', { 'form': form})
