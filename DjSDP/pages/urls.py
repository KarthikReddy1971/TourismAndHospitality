from django.urls import path

from .views import sample1,sample2,sample3,sample4,sample5,sample6,sample7,sample8
from . import views


urlpatterns = [
    path('',views.sample1,name='index'),
    path('destination/',views.sample2,name='destination'),
    path('travel/', views.sample3, name='travel'),
    path('login/', views.sample4, name='login'),
    path('regester/', views.sample5, name='register'),
    path('user/', views.sample6, name='user'),
    path('contact/',views.sample7,name='contact'),
    path('about/',views.sample8,name='about'),
]