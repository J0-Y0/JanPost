from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status = "published")
    
    options = (('draft','Draft'),
               ('published','Published')
                )
    title = models.CharField(max_length = 250)
    slug = models.SlugField(max_length = 250, unique_for_date = 'published_date')
    published_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    excerpt = models.TextField()
    content = models.TextField()
    status = models.CharField(max_length=15,choices=options,default='draft')
    objects = models.Manager()
    newManager = NewManager()
    class Meta:
        ordering =('-published_date',)
       
        verbose_name = 'Post'
        verbose_name_plural = 'posts'
    def __str__ (self):
        return self.title
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')  
    name  = models.CharField(max_length=50)
    email  = models.EmailField(max_length=50)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
    class  Meta:
        ordering = ('-published_date',)
        
    
    def __str__(self):
        return "commented by {self.name}"