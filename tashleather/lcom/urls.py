from django.urls import path, include
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
path('', views.index,name='index'),
    path('<id>/<str:slug>/', views.detail_view,name='details'),
    path('search/', views.search,name='search'),


]
