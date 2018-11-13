from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Post
# Create your views here.

class BlogListView(ListView):
	template_name="blog/blog_list.html"
	context_object_name = 'post'
	queryset = Post.objects.order_by('-published_date')


class BlogDetailView(DetailView):
	template_name='blog/blog_detail.html'
	context_object_name= 'post'

	def get(self, request, slug):
		queryset = get_object_or_404(Post, slug=slug)

		return render(request, self.template_name, {self.context_object_name:queryset})

