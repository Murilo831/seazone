from rest_framework import serializers
from .models import Imovel, Anuncio, Reserva

class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = '__all__'

class AnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

    def validate(self, data):
        data_checkin = data.get('data_checkin')
        data_checkout = data.get('data_checkout')

        if data_checkin and data_checkout:
            if data_checkin > data_checkout:
                raise serializers.ValidationError('A data de check-in não pode ser posterior à data de check-out')
            
        return data

        