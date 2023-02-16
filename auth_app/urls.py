from django.urls import path
from auth_app import views

urlpatterns = [
	path('login/', views.login, name="login"),
	path('logout/', views.logout, name="logout"),
	path('signup/', views.signup, name="signup"),

]