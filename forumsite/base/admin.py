from django.contrib import admin
from .models import Category, Post, UserBio, Comment, Tag


admin.site.register(Category)
admin.site.register(Tag)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'likes', 'updated', 'created')
    list_filter = ('category', )
    search_fields = ('title', )


@admin.register(UserBio)
class UserBioAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'country', 'company')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post_id', 'likes', 'updated', 'created')
