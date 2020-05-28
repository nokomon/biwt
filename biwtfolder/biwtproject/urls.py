from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import biwtapp.views
import ourapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('biwt/', include('ourapp.urls')),
    path('', biwtapp.views.home, name='home'),
    path('about/', biwtapp.views.about, name='about'),
    path('login/', biwtapp.views.login, name='login'),
    path('gaiphagi/', biwtapp.views.signup, name='signup'),
    path('logout/', biwtapp.views.logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
