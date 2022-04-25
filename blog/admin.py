from django.contrib import admin
from .models import Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ('created', 'author', 'published', 'status')
    date_hierarchy = 'published'
    raw_id_fields = ('author',)
    list_display = ('title', 'author', 'published', 'status')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}


