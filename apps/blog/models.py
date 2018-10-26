from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.SlugField(null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title