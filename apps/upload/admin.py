from django.contrib import admin
from .models import Video

# Register your models here.
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
	fields = ('author', 'title', 'description', 'slug', 'video', 'video_thumbnail', 'text', 'published_date')
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('author', 'title')