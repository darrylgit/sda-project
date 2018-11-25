from django.conf.urls import include, url

from .views import VideoIndexView, VideoListView, VideoDetailView

app_name = 'upload'

urlpatterns = [
	url(r'^$', VideoIndexView.as_view(), name='video_index'),
    url(r'^(?P<slug>[-\w]+)/?$', VideoListView.as_view(), name='video_list'),
    url(r'^(?P<slug>[-\w]+)/?$', VideoDetailView.as_view(), name='video_detail'),
]