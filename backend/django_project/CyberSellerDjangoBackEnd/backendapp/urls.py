from django.urls import path, re_path
from . import views
from django.views.static import serve
from CyberSellerDjangoBackEnd.settings import IMG_UPLOAD

urlpatterns = [
	path('', views.index, name='index'),
	path(r'signup', views.signup, name='signup'),
	path(r'login', views.login, name='login'),
	path(r'addGoods', views.addGoods, name='addGoods'),
	re_path(r'^img/(?P<path>.*)$', serve, {
		'document_root': IMG_UPLOAD
	}),
	path(r'mainRecommendGoods', views.mainRecommendGoods, name='mainRecommendGoods'),
	path(r'updateShopCart', views.updateShopCart, name='updateShopCart'),
	path(r'getGood', views.getGood, name='getGood'),
	path(r'searchShopCart', views.searchShopCart, name='searchShopCart'),
	path(r'updateStar', views.updateStar, name='updateStar')
]