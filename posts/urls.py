from django.conf.urls import url
#from django.contrib import admin
import posts
from . import  views # from . means from current directory
urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$',"posts.views.posts_home"),
    url(r'^create/$', "posts.views.post_create"),
    url(r'^detail/$', "posts.views.post_detail"),
    url(r'^update/$', "posts.views.post_update"),
    url(r'^delete/$', "posts.views.post_delete"),
]