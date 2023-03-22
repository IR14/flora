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
    # path('login/', views.registration, name='registration'),
    # path('graphics/', views.graphics, name='graphics')
    # path('login/', views.sign_in, name='login'),
    # path('logout/', views.sign_out, name='logout'),
    # path('register/', views.sign_up, name='register'),
    path('gallery/', views.gallery, name='gallery'),
    path('neuron/', views.neuron, name='neuron')
]
