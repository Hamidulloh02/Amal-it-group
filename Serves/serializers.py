from rest_framework import serializers

from Serves.models import Serves,Serves_list,Texnologies,Developers

class ServesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serves_list
        fields = (
            'id', 'title'
        )

class ServesTexnologiesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Texnologies
        fields = (
            'id','name','image'
        )
class ServesDevelopersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Developers
        fields = (
            'id','dev_name','dev_image'
        )
class ServesSerializers(serializers.ModelSerializer):
    serveslist = ServesListSerializer(many=True)
    texnologies = ServesTexnologiesSerializers(many=True)
    developers = ServesDevelopersSerializers(many=True)
    class Meta:
        model = Serves
        fields = (
                'id',
                'poster',
                'description',
                'serveslist',
                'texnologies',
                'developers',
        )
