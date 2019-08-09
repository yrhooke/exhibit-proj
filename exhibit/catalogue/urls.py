from django.urls import path
from . import views

urlpatterns = [
    path('', views.SearchView.as_view(), name='search'),
    path('searchbar', views.SearchBarView.as_view()),
    path('artwork', views.ArtworkList.as_view(), name="artwork_index"),
    path('artwork/new/', views.ArtworkCreate.as_view(), name='artwork_add'),
    path('artwork/<int:pk>/', views.ArtworkUpdate.as_view(), name='artwork_detail'),
    path('artwork/<int:pk>/delete/', views.ArtworkDelete.as_view(), name='artwork-delete'),
    path('series', views.SeriesList.as_view(), name="series_index"),
    path('series/new/', views.SeriesCreate.as_view(), name='series_add'),
    path('series/<int:pk>/', views.SeriesUpdate.as_view(), name='series_detail'),
    path('series/<int:pk>/delete/', views.SeriesDelete.as_view(), name='series-delete'),
    path('exhibition', views.ExhibitionList.as_view(), name="exhibition_index"),
    path('exhibition/new/', views.ExhibitionCreate.as_view(), name='exhibition_add'),
    path('exhibition/<int:pk>/', views.ExhibitionUpdate.as_view(), name='exhibition_detail'),
    path('exhibition/<int:pk>/delete/', views.ExhibitionDelete.as_view(), name='exhibition-delete'),
    path('location', views.LocationList.as_view(), name="location_index"),
    path('location/new/', views.LocationCreate.as_view(), name='location_add'),
    path('location/<int:pk>/', views.LocationUpdate.as_view(), name='location_detail'),
    path('location/<int:pk>/delete/', views.LocationDelete.as_view(), name='location-delete'),
    path('ajax_calls/search/', views.autocompleteView),
    path('ajax_calls/easy', views.ajaxEasyView),
]