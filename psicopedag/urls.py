from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls', namespace='pages')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG == False:
    handler400 = 'pages.views.error_400'
    handler403 = 'pages.views.error_403'
    handler404 = 'pages.views.error_404'
    handler500 = 'pages.views.error_500'

if "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns

if "google_analytics" in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path('djga/', include('google_analytics.urls')),
    ]