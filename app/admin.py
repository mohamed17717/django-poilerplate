from django.contrib import admin
from .models import Profile, WebRequest
# Register your models here.
admin.site.register(WebRequest)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
  def has_add_permission(self, request, obj=None):
    return False

  # This will help you to disable delete functionaliyt
  def has_delete_permission(self, request, obj=None):
    return False

  # This will help you to disable change functionality
  def has_change_permission(self, request, obj=None):
    return False