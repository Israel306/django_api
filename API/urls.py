from django.urls import path
from django.urls import include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, basename = 'login')

urlpatterns = [
    path("hello-view/", views.HelloApiView.as_view()), 
    path("", include(router.urls))
]
