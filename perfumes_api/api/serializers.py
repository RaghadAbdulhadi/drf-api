from rest_framework import serializers
from perfumes_api.models import Perfume

class PerfumeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'perfume_name', 'perfume_description')
        model = Perfume

# JSON
