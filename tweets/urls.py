from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tweets import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'users',views. UserViewSet)
router.register(r'tweets', views.TweetViewSet)
router.register(r'comments',views. CommentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]