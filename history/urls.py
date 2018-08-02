from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('artists/', views.ArtistView.as_view(), name="artists"),
    url(r'artists/\d', views.ArtistDetailView.as_view(), name="artist_detail")
]
