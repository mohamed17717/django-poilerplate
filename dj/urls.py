from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from app.views import error_page


handler404 = error_page(404)
handler500 = error_page(500)


urlpatterns = [
  path('app/', include('app.urls', namespace='app')),
  path('account/', include('accounts.urls', namespace='accounts')),

  path('admin/', admin.site.urls),
]

if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

  import debug_toolbar
  urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]