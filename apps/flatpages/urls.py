from django.conf.urls import include, url

from .views import AboutFlatpageView
from .views import ContactFlatpageView

app_name = 'flatpages'

urlpatterns =[
	url(r'^about-us/?$', AboutFlatpageView.as_view(), name='about_index'),
	url(r'^contact-us/?$', ContactFlatpageView.as_view(), name='contact_index')
]