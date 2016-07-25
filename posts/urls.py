from django.conf.urls import url
#from django.contrib import admin
import posts

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'$',"posts.views.posts_home"),
]