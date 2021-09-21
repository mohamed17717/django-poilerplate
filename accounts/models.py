from django.db import models
from django.contrib.auth import get_user_model

from .managers import AccountManager
from utils.models_mixins import OptimizeImageField

import secrets 


User = get_user_model()


class Account(models.Model):
  DEFAULT_USER_PICTURE = 'https://cdn2.iconfinder.com/data/icons/people-occupation-job/64/Ninja-Warrior-Assassin-Japan-Fighter-Avatar-Martial_arts-512.png'
  PICTURE_MINIMUM_DIMENSION = 200

  user = models.OneToOneField(User, related_name='user_account', on_delete=models.CASCADE)
  token = models.CharField(max_length=128, unique=True, editable=False, blank=True)

  picture = models.ImageField(upload_to='account_pictures', blank=True, null=True)

  created = models.DateField(auto_now_add=True)
  updated = models.DateField(auto_now=True)

  objects = AccountManager()

  class Meta:
    verbose_name = 'Account'
    verbose_name_plural = 'Accounts'

  def __str__(self):
    return self.user.username+f'({self.token})'

  def save(self, *args, **kwargs):
    if not self.pk:
      self.token = secrets.token_hex(nbytes=16)

    if self.picture:
      OptimizeImageField(self.picture, self.PICTURE_MINIMUM_DIMENSION)

    return super(Account, self).save(*args, **kwargs)


  # computed fields
  @property
  def get_username(self):
    name = f'{self.user.first_name} {self.user.last_name}'.strip() or self.user.username
    return name

  @property
  def get_picture(self):
    picture = self.picture and self.picture.url or self.DEFAULT_USER_PICTURE
    return picture


