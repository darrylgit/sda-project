from django.conf.urls import include, url

from .views import BlogIndexView, BlogListView, BlogDetailView

app_name = 'blog'

urlpatterns = [
	url(r'^$', BlogIndexView.as_view(), name='blog_index'),
	url(r'^posts/$', BlogListView.as_view(), name='blog_list'),
	url(r'^(?P<slug>[-\w]+)/?$', BlogDetailView.as_view(), name ='blog_detail'),
]
