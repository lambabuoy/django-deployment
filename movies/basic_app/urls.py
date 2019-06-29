from django.urls import path
from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.MovieListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.MovieDetailView.as_view(), name='detail'),
    path('create/', views.MovieCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', views.MovieUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.MovieDeleteView.as_view(), name='delete'),
    url(r'^search/', views.search, name='search')
]