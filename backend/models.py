from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    created = models.DateTimeField(auto_now=True)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, on_delete=models.CASCADE)

    @property
    def comment_count(self):
        # return Comment.objects.filter(post=self).count()
        return self.comment_set.all().count()

    @property
    def like_count(self):
        return self.likes_post.all().count()


class Comment(models.Model):
    post = models.ForeignKey(Post, blank=True, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s - %s' % (self.author, self.content)


class User(AbstractUser):
    username = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return "{}".format(self.username)

    @property
    def post_count(self):
        # return Post.objects.filter(author=self.user).count()
        return self.post_set.all().count()


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField(
        max_length=30, null=True, blank=True, unique=True)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to='profile_images')
    bio = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    followers = models.ManyToManyField("self", blank=True)
    following = models.ManyToManyField("self", blank=True)
    like_posts = models.ManyToManyField(
        Post, related_name='likes_post', blank=True)

    @property
    def followers_count(self):
        return self.followers.all().count()

    @property
    def following_count(self):
        return self.following.all().count()

    def __str__(self):
        return self.user.username


class Image(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE)
    image = models.FileField(upload_to='post_images')

    def __str__(self):
        return '%s' % (self.image)
