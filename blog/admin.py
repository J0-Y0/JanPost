from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "published_date", "reports")

    def reports(self, obj):
        return Report.objects.filter(post=obj).count()


class CommentAdmin(MPTTModelAdmin):
    list_display = ("post", "author", "content", "published_date")
    list_filter = ("status", "published_date")
    search_fields = ("author", "content")


class ReportAdmin(admin.ModelAdmin):
    list_display = ("post", "type", "author", "published_date")
    list_filter = ("type",)
    search_fields = ("post", "detail", "author")


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Report, ReportAdmin)
