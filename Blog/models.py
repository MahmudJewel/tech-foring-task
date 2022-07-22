from django.db import models
from Account.models import User

from tinymce.models import HTMLField
import datetime

from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
COMMENT_OPTIONS = (
    ('disabled', 'Disable Comments'),
    ('enabled', 'Enable Comments'),
)


class BlogCategory(models.Model):
    category = models.CharField(max_length=80)

    def __str__(self):
        return self.category

    @property
    def has_subcategories(self):
        if self.subcategory_category.all().count() > 0:
            return True
        else:
            return False

    class Meta:
        verbose_name_plural = 'Blog Categories'


class BlogSubCategory(models.Model):
    category = models.ManyToManyField(BlogCategory, related_name='subcategory_category', blank=True, null=True)
    sub_category = models.CharField(max_length=80)

    def __str__(self):
        return self.sub_category

    @property
    def has_filter(self):
        if self.filter_subcategory.all().count() > 0:
            return True
        else:
            return False

    class Meta:
        verbose_name_plural = 'Blog Sub Categories'


class FilterOption(models.Model):
    sub_category = models.ManyToManyField(BlogSubCategory, related_name='filter_subcategory', blank=True, null=True)
    filter_name = models.CharField(max_length=80)

    def __str__(self):
        return self.filter_name

    class Meta:
        verbose_name_plural = 'Blog Filter Option'


class Tags(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name_plural = 'Tags'


class Post(models.Model):
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE)
    post_url = models.CharField(max_length=264, verbose_name='URL', unique=True)
    title = models.CharField(max_length=264, verbose_name='Add Title')
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='post_category')
    sub_categories = models.ForeignKey(BlogSubCategory, on_delete=models.CASCADE, related_name='post_sub_category',
                                       blank=True, null=True)
    filter_option = models.ForeignKey(FilterOption, on_delete=models.CASCADE, related_name='post_filter',
                                      blank=True, null=True)
    feature_image = models.ImageField(upload_to='blog/', verbose_name='Add Feature Image')
    short_description = models.TextField(verbose_name='Short Description', max_length=264)
    content = HTMLField(verbose_name='Post Content')
    reading_time = models.DurationField(default=datetime.timedelta(minutes=3))
    comment_option = models.CharField(choices=COMMENT_OPTIONS, default='disabled', max_length=100)
    tag = models.ManyToManyField(Tags, related_name='post_tags', verbose_name='Add Tags')
    date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    total_view = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_post')
    comment = models.TextField(verbose_name='Comment', max_length=500)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post.title}\'s comment'


reading_status = (
    ('read', 'Read'),
    ('unread', 'Unread'),
)


class ReadingList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reading_list_user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reading_list_post')
    added_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, choices=reading_status, default='unread')

    def __str__(self):
        return f'{self.user} - {self.post}'

# class BlogSubscription(models.Model):
#     full_name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#
#     def __str__(self):
#         return f'{self.full_name} - {self.email}'


# @receiver(post_save, sender=Post)
# def send_email(sender, instance, created, *args, **kwargs):
#     if created:
#         print(BlogSubscription.objects.all())
