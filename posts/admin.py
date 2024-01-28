from django.contrib import admin

from posts.models import Post, Comments


class CommentInLine(admin.TabularInline):
    model = Comments
    extra = 0


@admin.action(description="Mark selected post as allowed")
def make_published(modeladmin, request, queryset):
    queryset.update(admin_allowed=True)


@admin.action(description="Mark selected post as not allowed")
def make_unpublished(modeladmin, request, queryset):
    queryset.update(admin_allowed=False)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]
    actions = [make_published, make_unpublished]


admin.site.register(Comments)
