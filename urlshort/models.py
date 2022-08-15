from django.db import models


class ShortUrl(models.Model):
    original_url = models.URLField(max_length=700)
    # short_url = domain.com/shorturl
    short_url = models.CharField(max_length=100)
    time_date_created = models.DateTimeField()

    def __str__(self):
        return self.original_url
