from rest_framework import serializers

from Portfolio.models import  Portfolio

class PortfolioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = (
                'id',
                'title',
                'poster',
                'subinfo',
                'created_at'
        )
