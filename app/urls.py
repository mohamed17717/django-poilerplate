from django.contrib import admin
from django.urls import path

from .views import (
  index,
  register_account,
  login_account,
  logout_account,
  static_template
)

app_name = 'app'


urlpatterns = [
  path('', index),

  path('register/', register_account.as_view(), name='register'),
  path('login/', login_account.as_view(), name='login'),
  path('logout/', logout_account, name='logout'),
  # static urls
  path('privacy-policy/', static_template('privacy.html'), name='privacy-policy'),
  path('about-us/', static_template('aboutus.html'), name='about-us'),
  path('contact-us/', static_template('contactus.html'), name='contact-us'),
]