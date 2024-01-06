from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from config import settings
urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('players/', include('players.urls')),
]

# Media files
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        'media/', document_root=settings.MEDIA_ROOT)
