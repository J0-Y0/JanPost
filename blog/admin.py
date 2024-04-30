from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin 
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','status','content','published_date', )
class CommentAdmin(MPTTModelAdmin):
    list_display = ('post','content','name','published_date' )
    list_filter = ('status','published_date')
    search_fields = ('name','email','content')
class ReportAdmin(admin.ModelAdmin):
    list_display = ('post','detail','type','name','published_date' )
    list_filter = ('post','type')
    search_fields = ('post','detail','name')

admin.site.register(Category)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Report,ReportAdmin)


