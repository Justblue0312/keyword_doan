from django.db import models


class GoogleWord(models.Model):
    google_word = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.google_word
