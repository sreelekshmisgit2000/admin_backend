from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet  # Correct import

router = DefaultRouter()
router.register(r'reviews', ReviewViewSet, basename='reviews')

urlpatterns = [
    path('', include(router.urls)),
]
