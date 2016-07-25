from django.conf.urls import url
#from django.contrib import admin
import posts
from .views import(
    posts_home,
    post_create,
    post_delete,
    post_detail,
    post_list,
    post_update) # from . means from current directory
urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$',posts_home),
    url(r'^create/$', post_create),
    url(r'^detail/$', post_detail),
    url(r'^update/$', post_update),
    url(r'^delete/$', post_delete),
]