from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
   

router = DefaultRouter()
router.register(r'carpets', CarpetViewSet, basename='carpet')

urlpatterns = [
    path('', include(router.urls)),
    path('colors/', ColorListView.as_view(), name='color-list'),    
    path('colors/<int:pk>/', ColorDetailView.as_view(), name='color-detail'),  
    path('designs/', DesignListView.as_view(), name='design-list'),    
    path('designs/<int:pk>/', DesignDetailView.as_view(), name='design-detail'), 
    path('sizes/rectangles/lengths/', LengthListView.as_view(), name='length-list'),
    path('sizes/rectangles/widths/', WidthListView.as_view(), name='width-list'),
    path('sizes/circles/radius/', RadiusListView.as_view(), name='radius-list'),
]
