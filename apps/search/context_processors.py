from .forms import ProjectModelSearchForm

def search_form(request):
    """
    Ensure that the search form is available site wide
    """
    return {'search_form': ProjectModelSearchForm(request.GET)}