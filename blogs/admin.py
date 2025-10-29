from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}  # JS auto-fills slug while typing
    list_display = ('title', 'slug','author','status')