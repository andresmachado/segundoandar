from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter(trailing_slash=False)
router.register(r'banners', views.BannerViewSet)
router.register(r'images', views.BannerImageViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]