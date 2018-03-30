from django.urls import path

from . import views

app_name = 'notes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:note_id>/', views.detail, name='detail'),
    path('<int:note_id>/results/', views.results, name='results'),
    path('<int:note_id>/vote/', views.vote, name='vote'),
]
