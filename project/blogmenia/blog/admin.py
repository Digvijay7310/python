from django.contrib import admin
from .models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'createdAt')
    search_fields = ('title', 'user__email')

admin.site.register(Blog, BlogAdmin)