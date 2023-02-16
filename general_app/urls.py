from django.urls import path
from general_app import views

urlpatterns = [
	path('terms/', views.terms, name="terms"),
	path('reach/', views.reach, name="reach"),
	path('safety/', views.safety, name="safety"),
	path('userhelp/', views.userhelp, name="userhelp"),
	path('advertisment/', views.advertisment, name="advertisment"),
]