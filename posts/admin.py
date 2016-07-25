from django.contrib import admin

# Register your models here.
from posts.models import Post

# MODEL ADMIN nije uvek neophodan, on se koristi samo kada je potrebno da se prosiri ono sto daje default:
#from posts.models import Post
#admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp", "updated", "content"]
    list_display_links = ["updated"]
    list_filter = ["updated", "timestamp", "title"]
    list_editable = ["title"]
    search_fields = ["title", "content"]
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)