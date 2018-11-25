from django.shortcuts import render, get_object_or_404

from django.views.generic import TemplateView, ListView, DetailView
from .models import Video

# Create your views here.
class VideoIndexView(ListView):
	template_name = "upload/video_index.html"

	def get(self, request):
		main = Video.objects.all().order_by('-published_date')[0]
		secondary = Video.objects.all().order_by('-published_date')[1:7]
		grid = Video.objects.all().order_by('-published_date')[7:]

		return render(request, self.template_name, {'main':main, 'secondary':secondary, 'grid':grid})

class VideoListView(ListView):
	context_object_name = "media"
	template_name = "upload/video_list.html"

	def get(self, request):
		queryset = Video.objects.all().order_by('-published_date')

		return render(request, self.template_name, {self.context_object_name:queryset})

class VideoDetailView(DetailView):
	context_object_name = "media"
	template_name ="upload/video_detail.html"
	model = Video

	def get_video_detail(self, request, slug):
		queryset=get_object_or_404(self.model, slug=slug)

		return render(request, self.template_name, {self.context_object_name: queryset})