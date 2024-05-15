from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone, text
from django.utils.timesince import timesince
from mptt.models import MPTTModel, TreeForeignKey
from taggit.managers import TaggableManager
import string
import random


# model field utility methods
# post based image directory
def postImageDirectory(instance, filename):
    return "posts/{0}/{1}".format(instance.id, filename)


# a random character to maintain slug uniqueness, append after title
def randomSlugPostfix():
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(6))


# models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="published")

    options = (("draft", "Draft"), ("published", "Published"))

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to=postImageDirectory, default="posts/default.jpg")
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1, null=True
    )
    excerpt = models.TextField()
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    status = models.CharField(max_length=15, choices=options, default="draft")

    favorite = models.ManyToManyField(
        User,
        default=None,
        blank=True,
        related_name="favorite",
    )
    liked = models.ManyToManyField(User, default=None, blank=True, related_name="liked")
    disliked = models.ManyToManyField(
        User, default=None, blank=True, related_name="disliked"
    )
    tags = TaggableManager()
    objects = models.Manager()
    newManager = NewManager()

    def time_difference(self):
        now = timezone.now()
        return timesince(self.published_date, now)

    class Meta:
        ordering = ("-published_date",)

        verbose_name = "Post"
        verbose_name_plural = "posts"

    def __str__(self):
        return self.title

    # overriding the save method
    def save(self, *args, **kwargs):

        if self.slug is None:
            self.slug = text.slugify(self.title + "_" + randomSlugPostfix())
        super().save(
            *args, **kwargs
        )  # Call the superclass's save() method to perform the actual save


class Comment(MPTTModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(User, default=None, blank=True, related_name="liked")

    status = models.BooleanField(default=True)

    def time_difference(self):
        now = timezone.now()
        # time_diff = now - self.created_at
        return timesince(self.published_date, now)

    class MPTTMeta:
        order_insertion_by = ["-published_date"]

    def __str__(self):
        return f"commented by {self.author}"


class Report(models.Model):
    report_types = (
        ("none_educational", "None Educational"),
        ("ethnic", "Ethnic Violence"),
        ("political", "Political Content"),
        ("explicit", "Explicit Content"),
        ("spam", "looks a spam"),
        ("other", "other"),
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="reports")
    name = models.CharField(max_length=50, verbose_name="Commented by")
    type = models.CharField(
        max_length=50, choices=report_types, verbose_name="Report type"
    )
    detail = models.TextField(verbose_name="Additional Details")
    published_date = models.DateTimeField(auto_now_add=True)

    def time_difference(self):
        now = timezone.now()
        # time_diff = now - self.created_at
        return timesince(self.published_date, now)

    class Meta:
        verbose_name = "Report"
        verbose_name_plural = "Reports"
        ordering = ("-published_date",)

    def __str__(self):
        return f"{self.name}:{self.type}"
