from django.db import models

# Create your models here.

class short_URL(models.Model):
    complete_url = models.URLField(max_length=250, primary_key=True)
    shortened_url = models.URLField(max_length=50)
    visits = models.IntegerField(default=0)

    def __str__(self):
        return self.complete_url