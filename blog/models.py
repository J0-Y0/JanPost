from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    options = (('draft','Draft'),
               ('published','Published')
                )
    title = models.CharField(max_length = 250)
    slug = models.SlugField(max_length = 250, unique_for_date = 'publish')
    published_date = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    content = models.TextField()
    status = models.CharField(max_length=15,choices=options,default='draft')
    def __str__ (self):
        return self.title
    