from django.contrib import admin
from .models import *
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','status','content','published_date', )
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','name','content','email','status','published_date' )
    list_filter = ('status','published_date')
    search_fields = ('name','email','content')

admin.site.register(Category)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)

