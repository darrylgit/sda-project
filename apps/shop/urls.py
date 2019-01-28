from django.conf.urls import include, url

from .views import ShopIndexView

app_name='shop'

urlpatterns = [
	url(r'^$', ShopIndexView.as_view(), name='shop_index'),
]