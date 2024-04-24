from django.contrib import admin
from .models import *
class PostAdmin(admin.ModelAdmin):
    fields = ['title','slug','published_date','author','content','status', ]

admin.site.register(Post,PostAdmin)
