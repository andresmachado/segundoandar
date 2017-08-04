from django.shortcuts import render
from rest_framework import viewsets

from .serializers import BannerSerializer, BannerImageSerializer
# Create your views here.

from cms.models import Banner, BannerImage

class BannerViewSet(viewsets.ModelViewSet):
    model = Banner
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()


class BannerImageViewSet(viewsets.ModelViewSet):
    model = BannerImage
    serializer_class = BannerImageSerializer
    queryset = BannerImage.objects.all()