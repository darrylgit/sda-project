from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from videokit.models import VideoField, VideoSpecField

# Create your models here.
class Video(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	description = models.SlugField(null=False)
	title = models.CharField(max_length=100, null = True)
	video = VideoField(upload_to = 'uploads/', null = True, blank = True,
    	mimetype_field = 'video_mimetype',
    	duration_field = 'video_duration',
    	thumbnail_field = 'video_thumbnail')
	video_thumbnail = models.ImageField(null = False, blank = True)
	text = models.TextField(null = False)
	published_date = models.DateTimeField(default=timezone.now)
	video_mimetype = models.CharField(max_length = 32, null = True, blank = True)
	video_duration = models.IntegerField(null = True, blank = True)
	video_mp4 = VideoSpecField(source = 'video', format = 'mp4')
	video_ogg = VideoSpecField(source = 'video', format = 'ogg')
	video_webm = VideoSpecField(source = 'video', format = 'webm')

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title


