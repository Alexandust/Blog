
from django.contrib import admin
from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author','views','comment_count']
    fields = ['title', 'body', 'excerpt', 'category', 'tags']
    ordering = ['-views'] #让博文按照浏览次数排序

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)