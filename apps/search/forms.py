from django import forms
from haystack.forms import *
from django.utils.translation import ugettext_lazy as _




class ProjectSearchForm(SearchForm):
    q = forms.CharField(required=False, label=_('Search'),
                        widget=forms.TextInput(attrs={'type': 'search'}))
    q.widget.attrs.pop("autofocus", None)

class ProjectModelSearchForm(ProjectSearchForm):
    def __init__(self, *args, **kwargs):
        super(ProjectModelSearchForm, self).__init__(*args, **kwargs)
        self.fields['models'] = forms.MultipleChoiceField(choices=model_choices(), required=False, label=_('Search In'), widget=forms.CheckboxSelectMultiple)
