from django.conf.urls import url
from basic_app import views
#Template tagging

app_name ='basic_app'


urlpatterns = [
    url(r'^relative/',views.relative_url_temp,name ='relative_url_temp'),
    url(r'^other/',views.other,name='other'),
    url(r'^index',views.index,name='index'),
]
