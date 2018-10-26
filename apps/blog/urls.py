from django.conf.urls import include, url

from .views import BlogListView, BlogDetailView

app_name = 'blog'

urlpatterns = [
	url(r'^$', BlogListView.as_view(), name='blog_index'),
	url(r'^(?P<description>[-\w]+)-(?P<pk>\d+)/?$', BlogDetailView.as_view(), name ='blog_detail'),
]
