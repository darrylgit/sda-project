from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

class ShopIndexView(TemplateView):
	template_name = 'shop/shop_index.html'

	def get_template(self, request):

		return render(request, self.template_name, {})
