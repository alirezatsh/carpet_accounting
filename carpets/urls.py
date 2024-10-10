from django.urls import path
from . import views

urlpatterns = [
    path('colors/', views.ColorListView.as_view(), name='color-list'),    
    path('colors/<int:pk>/', views.ColorDetailView.as_view(), name='color-detail'),  
    path('designs/', views.DesignListView.as_view(), name='design-list'),    
    path('designs/<int:pk>/', views.DesignDetailView.as_view(), name='design-detail'), 
    path('carpets/', views.CarpetListView.as_view(), name='carpet-list'),       
    path('carpets/<int:pk>/', views.CarpetDetailView.as_view(), name='carpet-detail'),
    path('sizes/rectangles/lengths/', views.LengthListView.as_view(), name='length-list'),
    path('sizes/rectangles/widths/', views.WidthListView.as_view(), name='width-list'),
    path('sizes/circles/radius/', views.RadiusListView.as_view(), name='radius-list'),
]
