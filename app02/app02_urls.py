from django.conf.urls import url
from app02 import views

urlpatterns = [
   url(r'user/$', views.user)
]