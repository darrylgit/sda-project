from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Post

# Create your views here.

class BlogListView(ListView):
	template_name="blog/blog_list.html"
	context_object_name = 'blog'
	model = 'Post'

	def get(self, request):
		queryset = Post.objects.all()

		return render(request, self.template_name, {self.context_object_name:queryset})

class BlogDetailView(DetailView):
	template_name='blog/blog_detail.html'
	context_object_name= 'blog'
	model='Post'

	def get(self, request, description, pk):
		queryset = get_object_or_404(Post, description=description, pk=pk)

		return render(request, self.template_name, {self.context_object_name:queryset})

