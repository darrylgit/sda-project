from haystack.forms import ModelSearchForm

def search_form(request):
    """
    Ensure that the search form is available site wide
    """
    return {'search_form': ModelSearchForm(request.GET)}