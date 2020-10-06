from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name='home'),
    path('flashcards/', include('flashcards_app.urls')),
    path('api/v1.0/', include('farmacias_turno_app.urls'),),
    path('api/v1.0/', include('portfolio_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
