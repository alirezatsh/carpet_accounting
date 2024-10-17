from . import views
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import WorkerViewSet, HelpWorkerViewSet

# تعریف روت‌ها برای ViewSet ها
router = DefaultRouter()
router.register(r'workers', WorkerViewSet)
router.register(r'helps', HelpWorkerViewSet)  # اضافه کردن HelpViewSet

urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('sections/', views.SectionListView.as_view(), name='section-list'),
    path('sections/chelleh/', views.WorkersBySectionView.as_view(), {'section_name': 'چله کشی'}, name='chaleh-workers'),
    path('sections/shirazeh/', views.WorkersBySectionView.as_view(), {'section_name': 'شیرازه'}, name='shiraze-workers'),
    path('sections/gereh/', views.WorkersBySectionView.as_view(), {'section_name': 'گره زن'}, name='gereh-workers'),
    path('token-verify/', views.TokenVerifyView.as_view(), name='token-verify'),

]
