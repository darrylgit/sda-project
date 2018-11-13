from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView
from .models import Video

# Create your views here.
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