from django.contrib import admin
from django.urls import path

from .views import index, static_template

app_name = 'app'


urlpatterns = [
  path('', index),

  # static urls
  path('privacy-policy/', static_template('privacy.html'), name='privacy-policy'),
  path('about-us/', static_template('aboutus.html'), name='about-us'),
  path('contact-us/', static_template('contactus.html'), name='contact-us'),
]