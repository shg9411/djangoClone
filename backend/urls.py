from django.urls import path,include
from backend import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts',views.PostViewSet)
router.register('users', views.UserViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
