from rest_framework import serializers
from .models import Travel, Klass, Mehmonxona

class KlassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klass
        fields = '__all__'

class MehmonxonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mehmonxona
        fields = '__all__'

class TravelSerializer(serializers.ModelSerializer):
    klass = KlassSerializer()
    mehmonxona = MehmonxonaSerializer()

    class Meta:
        model = Travel
        fields = '__all__'
