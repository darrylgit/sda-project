from django.shortcuts import render

from haystack.generic_views import SearchView
#from .forms import VideoSearchForm

# Create your views here.
class VideoSearchView(SearchView):
	"""
    A modified version of Haystack's SearchView
    """
	template_name="search/results.html"