from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from .models import Video

# Create your views here.
class VideoIndexView(TemplateView):
	context_object_name = "media"
	template_name = "upload/video_index.html"
	model = Video
	context = {}
	def get(self, request):
		try:
			self.context['primary'] = self.model.objects.all().order_by('-published_date')[0]
			self.context['secondary'] = self.model.objects.all().order_by('-published_date')[1:7]
			self.context['grid'] = self.model.objects.all().order_by('-published_date')[7:]

			return render(request, self.template_name, {self.context_object_name:self.context})

		except IndexError:

			return HttpResponse("Sorry, This page is under construction...") 

class VideoListView(ListView):
	context_object_name = "media"
	template_name = "upload/video_list.html"

	def get(self, request):
		queryset = Video.objects.all().order_by('-published_date')

		return render(request, self.template_name, {self.context_object_name:queryset})

class VideoDetailView(TemplateView):
	context_object_name = "media"
	template_name ="upload/video_detail.html"
	model = Video
	context={}

	def get(self,request, slug):
		self.context['primary'] = get_object_or_404(self.model, slug=slug)
		self.context['secondary'] = self.model.objects.all().order_by('-published_date')[1:7]
		self.context['grid'] = self.model.objects.all().order_by('-published_date')[7:]

		return render(request, self.template_name, {self.context_object_name: self.context})

