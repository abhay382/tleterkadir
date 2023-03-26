"""tashleather URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from com import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Leather/', include('lcom.urls')),
    path('',views.index,name='index'),
    path('about/',views.About,name='about'),
    path('contact/', views.contact, name='contact'),
    path('Gallery/', views.Gallery, name='gallery'),
    path('Leather-journal-manufacturer/', views.Leatherj, name='Leather-journal-manufacturer'),
    path('embossed-leather-manufacturer/', views.Leatherej, name='embossed-leather-manufacturer'),
    path('Vintage-leather-journal/', views.Leatherevj, name='Leatherevj'),
    path('Leather-Duffle-Bags-manufacturer/', views.Leatherdufflebag, name='Leatherdufflebag'),
    path('Leather-Backpacks-manufacturer/', views.Leatherbackpack, name='Leatherbackpackbag'),
    path('Leather-Sling-Bags-manufacturer/', views.Leatherslingbag, name='Leatherslingbag'),
    path('Leather-Tote-Bags-manufacturer/', views.Leathertotebag, name='Leatherslin'),
    path('Leather-Messenger-Bags-manufacturer/', views.Leathermessangerbag, name='Leatherslin'),
    path('Leather-Laptop-Bags-manufacturer/', views.Leatherlaptopbag, name='Leatherslin'),
    path('Leather-Briefcase-&-Bags/', views.Leatherbriefcase, name='Leatherslin'),
    path('Leather-Wash-Bags-Toiletry-Bags/', views.Leatherwashbag, name='Leatherslin'),
    path('Leather-Saddle-Bags-manufacturer/', views.Leathersaddlebag, name='Leatherslin'),
    path('Leather-Hobo-Bags/', views.hobo, name='Leatherslin'),
    path('Leather-bag-manufacturer/', views.Lb, name='Leatherslin'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)