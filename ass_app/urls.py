from django.urls import path
from .views import *
# from ilpapi import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("api/messages/", MessageAPIView.as_view(),name='message')
    # path("user/", UserAPIView.as_view(),name='user'),
    ]        
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 