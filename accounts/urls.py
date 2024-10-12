from . import views
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.schemas import get_schema_view



urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('sections/', views.SectionListView.as_view(), name='section-list'),
    path('workers/' , views.WorkerListView.as_view() , name='users'),
    path('sections/chelleh/', views.WorkersBySectionView.as_view(), {'section_name': 'چله کشی'}, name='chaleh-workers'),
    path('sections/shirazeh/', views.WorkersBySectionView.as_view(), {'section_name': 'شیرازه'}, name='shiraze-workers'),
    path('sections/gereh/', views.WorkersBySectionView.as_view(), {'section_name': 'گره زن'}, name='shiraze-workers'),
    path('workers/add/', views.WorkerDetailView.as_view(), name='add-worker'), 
    path('workers/<int:pk>/update/', views.WorkerDetailView.as_view(), name='update-worker'),  
    path('workers/<int:pk>/delete/', views.WorkerDetailView.as_view(), name='delete-worker'),



]
