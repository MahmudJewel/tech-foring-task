from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('BusinessSecurity.urls')),
    path('mysecurity/', include('PersonalSecurity.urls')),
    path('academy/', include('Academy.urls')),
    path('account/', include('Account.urls')),
    path('', include('Blog.urls')),
    path('api/', include('Api.urls')),
    path('accounts/', include('allauth.urls')),
    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'BusinessSecurity.views.error_404_handler'