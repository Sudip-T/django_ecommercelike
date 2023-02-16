from django.urls import path
from ecom_app import views

urlpatterns = [
	path('', views.store, name="home"),
	path('cart/', views.cart, name="cart"),
    path('search/', views.search, name="search"),
	path('checkout/', views.checkout, name="checkout"),
    path('categoryproducts/<int:id>', views.category_products, name="category_products"),
    path('searchlist/', views.searchlist, name="searchlist"),
    path('singleproduct/<int:id>', views.singleproduct, name="singleproduct"),

]