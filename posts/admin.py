from django.contrib import admin

from posts.models import Post, Comments


class CommentInLine(admin.TabularInline):
    model = Comments
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]


admin.site.register(Comments)
