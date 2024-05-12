from django.db import models
from django.contrib.auth.models import User


class UserBio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)
    country = models.CharField(max_length=255, blank=True)
    company = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = 'UserBio'
        verbose_name_plural = 'UserBios'


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=True, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']


class Tag(models.Model):
    name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['name']


class Post(models.Model):
    category = models.ForeignKey(Category, models.DO_NOTHING)
    author = models.ForeignKey(User, models.DO_NOTHING)

    title = models.CharField(max_length=100, blank=True, null=False)
    content = models.TextField(blank=True, null=False)
    image = models.TextField(blank=True)

    likes = models.IntegerField(default=0, blank=False)
    tags = models.ManyToManyField(Tag)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-updated', '-created', '-likes']


class Comment(models.Model):
    post_id = models.IntegerField(null=False)
    author = models.ForeignKey(User, models.DO_NOTHING)
    content = models.TextField(blank=True, null=False)

    likes = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[:20]

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
