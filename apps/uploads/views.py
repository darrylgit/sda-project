from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView
from .models import Video

# Create your views here.
class VideoListView(ListView):
	context_object_name = "upload_obj"
	template_name = "uploads/video_list.html"

	def get(self, request):
		queryset = Video.objects.all().order_by('-published_date')

		return render(request, self.template_name, {'upload_obj':queryset})

class VideoDetailView(DetailView):
	context_object_name = "videoDetail"
	template_name ="uploads/video_detail.html"
	model = Video

	def get_video_detail(self, request, pk):
		videoDetail =get_object_or_404(self.model, pk=pk)

		return render(request, self.template_name, {'videoDetail': videoDetail})