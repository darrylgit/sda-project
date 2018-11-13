from django.conf.urls import include, url

from .views import BlogListView, BlogDetailView

app_name = 'blog'

urlpatterns = [
	url(r'^$', BlogListView.as_view(), name='blog_index'),
	url(r'^(?P<slug>[-\w]+)/?$', BlogDetailView.as_view(), name ='blog_detail'),
]
