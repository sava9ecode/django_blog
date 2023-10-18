from django.contrib import admin

from .models import Category, Post, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title",)
    list_filter = (
        "created_on",
        "last_modified",
    )
    fields = (
        "title",
        "body",
        "categories",
    )
    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ("created_on",)
