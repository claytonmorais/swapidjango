from rest_framework import serializers
from api.models import Film,Planet,People,Vehicle,Species,Starship

class FilmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'

class PlanetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = '__all__'

class PeoplesSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = '__all__'

class VehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class StarShipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Starship
        fields = '__all__'

class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = '__all__'
