from django.contrib import admin
from .models import Post,Comments
# Register your models here.

@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','body','post', 'date')
    list_filter = ('date',)
    search_fields = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ('category','date')
