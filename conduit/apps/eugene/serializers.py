from rest_framework import serializers
from .models import Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('country', 'slug')

    # def to_representation(self, obj):
    #     return obj.country
