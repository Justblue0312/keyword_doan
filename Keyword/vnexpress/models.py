from django.db import models
import uuid


class NewsPost(models.Model):
    title = models.CharField(max_length=50000, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    intro = models.CharField(max_length=50000, blank=True, null=True)
    url = models.URLField(max_length=1000, blank=True, null=True)
    keywords = models.CharField(max_length=50000, blank=True, null=True)
    content = models.CharField(max_length=1000000, blank=True, null=True)
    image = models.CharField(max_length=1000, blank=True, null=True)
    published_date = models.CharField(max_length=255, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
