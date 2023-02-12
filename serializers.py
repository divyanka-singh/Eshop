from rest_framework import serializers
from .models import signup

# Serializers define the API representation.


class eshopserializer(serializers.ModelSerializer):
    class Meta:
        model = signup
        fields = '__all__'
