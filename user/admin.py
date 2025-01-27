from django.contrib import admin
from user.models import Profile

admin.site.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'image')
    list_filter = ('user')