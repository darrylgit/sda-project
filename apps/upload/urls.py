from django.conf.urls import include, url

from .views import VideoListView, VideoDetailView

app_name = 'upload'

urlpatterns = [
    url(r'^$', VideoListView.as_view(), name='video_index'),
    url(r'^videos/(?P<slug>[-\w]+)/?$', VideoDetailView.as_view(), name='video_detail'),
]