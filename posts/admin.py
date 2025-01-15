from django.contrib import admin
from .models import Post, Category,Tag

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'category', 'created_at']
    list_filter = ['category', 'tag']
    search_fields = ['title', 'content']

admin.site.register(Tag)
admin.site.register(Category)