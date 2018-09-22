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
from django.views.static import serve
from django.conf import settings
from django.shortcuts import HttpResponse


def d1(requests):
    return HttpResponse("OK")


urlpatterns = [
    url(r'^$', views.list_book, name="home"),
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
    url(r'^ajax_deletebook/', views.ajax_deletebook),

    url(r'^list_author/', views.list_author),
    url(r'^delete_author/', views.delete_author),
    url(r'^add_author/', views.add_author),
    url(r'^edit_author/', views.edit_author),
    url(r'^t_filter/', views.t_filter),
    url(r'delete/(?P<table_name>\w+)/(?P<row_id>\d+)', views.delete_action),

    url(r'index/', views.index, name="index"),
    url(r'^upload/$', views.upload_file.as_view()),
    url(r'^login/$', views.login, name="login"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^ajax_html/$', views.ajax_html),
    url(r'ajax_get', views.ajax_get),
    url(r'ajax_post', views.ajax_post),
    url(r'serialization', views.serialization),
    url(r'^auth_login/$', views.auth_login),
    url(r'^auth_logout/$', views.auth_logout),
    url(r'^auth_reg/$', views.auth_reg),

    # form 组件
    url(r'^register/$', views.register),
    # media相关的路由设置
    url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
    url(r'kind_upload/$', views.kind_upload),

    # 多应用URL
    url(r"app02/", include("app02.app02_urls")),

    # 根据Django admin实现URL分发.
    url(r"^dispath/", ([url(r'^d1/$', d1), url(r'^d2/$', d1), url(r'^d3/$', d1)], None, None))
]
