from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post
# Create your views here.

class BlogIndexView(TemplateView):
	context_object_name="post"
	template_name="blog/blog_index.html"
	model=Post
	context = {}
	def get(self, request):
		try:
			self.context['primary'] = self.model.objects.all().order_by('-published_date')[0]
			self.context['grid'] = self.model.objects.all().order_by('-published_date')[1:]

			return render(request, self.template_name, {self.context_object_name:self.context})

		except IndexError:

			return HttpResponse("Sorry, This page is under construction...") 

class BlogListView(ListView):
	context_object_name = 'post'
	template_name="blog/blog_list.html"
	model = Post

	def get(self,request):
	    post_list = self.model.objects.all().order_by('-published_date')
	    paginator = Paginator(post_list, 3) # Show 2 posts per page
	    page = request.GET.get('page')
	    try:
	        posts = paginator.page(page)
	    except PageNotAnInteger:
	        # If page is not an integer, deliver first page.
	        posts = paginator.page(1)
	    except EmptyPage:
	        # If page is out of range (e.g. 9999), deliver last page of results.
	        posts = paginator.page(paginator.num_pages)

	    return render(request, self.template_name, {self.context_object_name: posts})


class BlogDetailView(DetailView):
	context_object_name= 'post'
	template_name='blog/blog_detail.html'
	
	def get(self, request, slug):
		queryset = get_object_or_404(Post, slug=slug)

		return render(request, self.template_name, {self.context_object_name:queryset})

