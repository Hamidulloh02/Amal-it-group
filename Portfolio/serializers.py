from rest_framework import serializers

from Portfolio.models import  Portfolio,Image

class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'id',
            'image'
        )

class PortfolioSerializers(serializers.ModelSerializer):
    images = ImageSerializers(many=True)
    class Meta:
        model = Portfolio
        fields = (
                'id',
                'title',
                'poster',
                'images',
                'subinfo',
                'created_at'
        )
