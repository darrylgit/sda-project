import datetime
from haystack import indexes
from .models import Video


class VideoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    published_date = indexes.DateTimeField(model_attr='published_date')

    def get_model(self):
        return Video

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()