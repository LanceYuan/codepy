"""codepy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^$', views.list_book),
    url(r'^admin/', admin.site.urls),
    url(r'^publisher_list/', views.publisher_list),
    url(r'^delete_publisher/(\d+)/', views.delete_publisher),
    # url(r'^add_publisher/', views.add_publisher),
    url(r'^add_publisher/', views.AddPublisher.as_view()),
    url(r'^edit_publisher/', views.edit_publisher),

    url(r'^list_book/', views.list_book),
    url(r'^add_book/', views.add_book),
    url(r'^delete_book/', views.delete_book),
    url(r'^edit_book/', views.edit_book),

    url(r'^list_author/', views.list_author),
    url(r'^delete_author/', views.delete_author),
    url(r'^add_author/', views.add_author),
    url(r'^edit_author/', views.edit_author),
    url(r'^t_filter/', views.t_filter),
    url(r'delete/(?P<table_name>\w+)/(?P<row_id>\d+)', views.delete_action),

    url(r'index/', views.index, name="index"),
    url(r'upload/', views.upload_file.as_view()),

    # 多应用URL
    url(r"app02/", include("app02.app02_urls")),
]
