from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='index'),
    path('addmovie/', views.addmovie_view, name='addmovie'),
    path('showmovies/', views.showmovies_view, name='showmovies'), 
]
