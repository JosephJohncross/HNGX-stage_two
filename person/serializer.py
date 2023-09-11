from rest_framework import serializers
from .models import Person


class GetPersonSerializer(serializers.ModelSerializer):
    """Serializer that returns/updates a user object"""

    class Meta:
        model = Person
        fields = ['name', 'id']


class GeneralPersonSerializer(serializers.ModelSerializer):
    """Serializer for all other operations performed on a person"""

    class Meta:
        model = Person
        fields = ['name']
