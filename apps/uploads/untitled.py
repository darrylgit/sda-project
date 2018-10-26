from django.db import models

from django.utils import timezone

from videokit.models import VideoField

# Create your models here.
class Video(models.Model):
	title = models.CharField(max_length=100, default='Video Title')
	upload = models.FileField(upload_to='uploads/')
	published_date = models.DateTimeField(default=timezone.now)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __unicode__(self):
		return self.title