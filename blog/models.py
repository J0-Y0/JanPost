from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from mptt.models import MPTTModel,TreeForeignKey

def postImageDirectory(instance,filename):
    return 'posts/{0}/{1}'.format(instance.id,filename)

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status = "published")
    
    options = (('draft','Draft'),
               ('published','Published')
                )
    title = models.CharField(max_length = 250)
    slug = models.SlugField(max_length = 250, unique_for_date = 'published_date')
    image = models.ImageField(upload_to=postImageDirectory,default='posts/default.jpg')
    
   
    category = models.ForeignKey(Category, on_delete=models.PROTECT,default=1)

    excerpt = models.TextField()
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    status = models.CharField(max_length=15,choices=options,default='draft')
    
    objects = models.Manager()
    newManager = NewManager()
    class Meta:
        ordering =('-published_date',)
       
        verbose_name = 'Post'
        verbose_name_plural = 'posts'
    def __str__ (self):
        return self.title
class Comment(MPTTModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments') 
    parent = TreeForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name="children" )
    name  = models.CharField(max_length=50 ,verbose_name='Commented by')
    email  = models.EmailField(max_length=50)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
    class MPTTMeta:
        order_insertion_by = ['-published_date']
        
    def __str__(self):
        return f"commented by {self.name}"