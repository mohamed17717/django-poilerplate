from django.db import models
from django.contrib.auth import get_user_model

from jsonfield import JSONField


User = get_user_model()


# Create your models here.
class Profile(models.Model):
  user = models.ForeignKey(User, related_name='user_profile', on_delete=models.CASCADE)
  name = models.CharField(max_length=50, blank=True, null=True)
  age = models.IntegerField(blank=True, null=True)

  picture = models.ImageField(upload_to='thumbnails', default='thumbnails/default.jpg')
  shitty_data = JSONField()

  def serialize(self):
    return {
      'user': self.user.__dict__,
      'name': self.name,
      'age': self.age
    }

