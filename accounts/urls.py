from django.urls import path

from .views import (
  register_account,
  login_account,
  logout_account,
)

app_name = 'accounts'


urlpatterns = [
  path('register/', register_account.as_view(), name='register'),
  path('login/', login_account.as_view(), name='login'),
  path('logout/', logout_account, name='logout'),
]