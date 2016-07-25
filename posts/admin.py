from django.contrib import admin

# Register your models here.
from posts.models import Post

# MODEL ADMIN nije uvek neophodan, on se koristi samo kada je potrebno da se prosiri ono sto daje default:
#from posts.models import Post
#admin.site.register(Post)
admin.site.register(Post)