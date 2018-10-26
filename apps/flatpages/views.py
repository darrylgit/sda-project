from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

class AboutFlatpageView(TemplateView):
	template_name = 'flatpages/about_flatpage.html'

	def get_template(self, request):

		return render(request, self.template_name, {})

class ContactFlatpageView(TemplateView):
	template_name='flatpages/contact_flatpage.html'

	def get_template(self, request):

		return render(request, self.template_name, {})
	
