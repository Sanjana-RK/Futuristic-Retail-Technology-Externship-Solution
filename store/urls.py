from django.urls import path,include,re_path
from . import views

#Defining the app name, I have defined it as store
app_name = 'store'


#Defining urlpatterns to process request
urlpatterns = [
    path('',views.storeitems,name="storeit"),
    path('addstoreitems/',views.store_create, name="list"),
    re_path(r'^create/$',views.store_create, name="create"),
]
