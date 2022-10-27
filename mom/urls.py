from django.urls import path

from .views import DogDeleteView, DogDetailView, DogListView, DogUpdateView
from . import views

urlpatterns = [
    path('', DogListView.as_view(), name='dog_list'),
    path('<int:pk>/', DogDetailView.as_view(), name='dog_detail'),
    path('<int:pk>/edit/', DogUpdateView.as_view(), name='dog_edit'),
    path('<int:pk>/delete/', DogDeleteView.as_view(), name='dog_delete'),
    path('query1/', views.query1, name='db_query1'),
    path('query2/', views.query2, name='db_query2'),
    path('query3/', views.query3, name='db_query3'),
    path('query4/', views.query4, name='db_query4'),
    path('query5/', views.query5, name='db_query5'),
    path('query6/', views.query6, name='db_query6'),
    path('query7/', views.query7, name='db_query7'),

]
