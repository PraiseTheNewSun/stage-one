from rest_framework import serializers #type: ignore
from .models import StringModel

class StringSerializer(serializers.ModelSerializer):
    class Meta:
        model = StringModel
        # fields = ['string']
        fields = '__all__'

class AnalyzedStringSerializer(serializers.ModelSerializer):
    class Meta:
        model = StringModel
        fields = '__all__'