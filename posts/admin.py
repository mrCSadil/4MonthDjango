from django.contrib import admin
from .models import Post, Category,Tag

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'category', "author", 'created_at', 'rate']
    list_filter = ['category', 'tag', 'author']
    search_fields = ['title', 'content', "tags__name"]
    list_editable = ['rate']


admin.site.register(Tag)
admin.site.register(Category)