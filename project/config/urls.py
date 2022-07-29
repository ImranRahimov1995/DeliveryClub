from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from apps.delivery_club.views import DeliveryRecordsDashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DeliveryRecordsDashboard.as_view(), name='dashboard')
]

# Local settings
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
