from django.contrib import admin
from django.conf.urls import include
from django.urls import path,include,re_path
from .import views


#Defining urlpatterns to process request
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('store/',include('store.urls')),
]
