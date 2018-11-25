from django.conf.urls import include, url

from .views import IndexFlatpageView, AboutFlatpageView, ContactFlatpageView

app_name = 'flatpage'

urlpatterns =[
	url(r'^$', IndexFlatpageView.as_view(), name='index'),
	url(r'^about-us/?$', AboutFlatpageView.as_view(), name='about_index'),
	url(r'^contact-us/?$', ContactFlatpageView.as_view(), name='contact_index')
]