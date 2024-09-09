from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from .views import language_switch, handler404
from . import views

# Define the URL patterns for the app
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Include Django Allauth URLs
    path('properties/', include('properties.urls')),
    path('construction/', include('construction.urls')),
    path('profiles/', include('profiles.urls')),
    path('contact/', include('contact.urls')),
    path('', include('residenza.urls')), 
]

# Add language switching URL pattern outside i18n_patterns
urlpatterns += [
    path('language/<str:lang_code>/', language_switch, name='language_switch'),
]

# Adding i18n_patterns to handle language prefixes
urlpatterns += i18n_patterns(
    # Your main app URLs with language prefixes
    path('properties/', include('properties.urls')),
    path('construction/', include('construction.urls')),
    path('profiles/', include('profiles.urls')),
    path('contact/', include('contact.urls')),
    path('', include('residenza.urls')), 
    prefix_default_language=True  # This will add /en/ prefix for English
)

# Serve static files (only in development; for production use a web server)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom 404 error handler
handler404 = 'residenza127.views.handler404'
