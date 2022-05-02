from django.db import models
from ckeditor.fields import RichTextField
import uuid


class ArticleNews(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    abstract = models.CharField(max_length=10000, blank=True, null=True)
    url = models.URLField()
    content = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    image_url = models.URLField()
    attribution = models.CharField(max_length=255, null=True, blank=True)
    image_name = models.CharField(max_length=5000, null=True, blank=True)
    image_caption = models.CharField(max_length=5000, null=True, blank=True)
    source = models.CharField(max_length=255, null=True, blank=True)
    reaction_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta():
        ordering = ['publish_date']


class SliceNews(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    body_html = RichTextField(null=True, blank=True)
    url = models.URLField()
    image_url = models.URLField()
    image_name = models.CharField(max_length=5000, null=True, blank=True)
    image_caption = models.CharField(max_length=5000, null=True, blank=True)
    attribution = models.CharField(max_length=5000, null=True, blank=True)
    source = models.CharField(max_length=255, null=True, blank=True)
    publish_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta():
        ordering = ['publish_date']
