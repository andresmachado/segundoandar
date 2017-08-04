from rest_framework import serializers
from cms.models import Banner, BannerImage


class BannerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImage
        exclude = ('id', )


class BannerSerializer(serializers.ModelSerializer):
    images = BannerImageSerializer(many=True, read_only=True)

    class Meta:
        model = Banner
        exclude = ('id', )