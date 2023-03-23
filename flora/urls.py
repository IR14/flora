from django.urls import path
from . import views

app_name = 'flora'
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),

    path('houseplants/', views.houseplants, name='houseplants'),
    path('bouquets/', views.bouquets, name='bouquets'),
    path('street/', views.street, name='street'),
    path('feedback/', views.feedback, name='feedback'),
    path('gallery/', views.gallery, name='gallery'),

    path('shop/', views.shop, name='shop'),
    path('article/', views.article, name='article'),
    path('test/', views.test, name='test'),
    path('animation/', views.animation, name='animation'),

    path('neuron/', views.neuron, name='neuron'),
    path('graphics/', views.graphics, name='graphics'),
    path('care/', views.care, name='care'),
    path('neuroart/', views.neuroart, name='neuroart'),
    path('calculator/', views.calculator, name='calculator')
]
