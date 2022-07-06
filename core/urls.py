from django.urls import path
from . import views
urlpatterns=[
    path('',views.djhome),
    path('about',views.djaboutus),
    path('contact',views.djcontactus),
    path('home',views.djhome),
    path('join',views.djjoinus),
    path('services',views.djservices),
    path('trainers',views.djtrainers),
]