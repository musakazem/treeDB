from django.urls import path
from . import views

urlpatterns = [
	
	path('search-results/', views.showResults, name = 'showResults'),
	path('', views.search, name = 'search'),
	path('detail-page/<str:plate_no>/', views.showDetails, name = 'showDetails'),
]