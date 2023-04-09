from rest_framework import viewsets, generics
from api.models import Film, People, Vehicle, Planet, Starship, Species
from api.serializer import FilmsSerializer, PlanetsSerializer, PeoplesSerializer, VehiclesSerializer,StarShipsSerializer,SpeciesSerializer
from api.loader import exec
from django.http import JsonResponse

# Create your views here.
class FilmsViewSet(viewsets.ModelViewSet):
    """SHOW TO FILMS"""
    queryset = Film.objects.all()
    serializer_class = FilmsSerializer

class PlanetsViewSet(viewsets.ModelViewSet):
    """SHOW TO PLANETS"""
    queryset = Planet.objects.all()
    serializer_class = PlanetsSerializer

class PeoplesViewSet(viewsets.ModelViewSet):
    """SHOW TO PEOPLES"""
    queryset = People.objects.all()
    serializer_class = PeoplesSerializer

class VehiclesViewSet(viewsets.ModelViewSet):
    """SHOW TO VEHICLES"""
    queryset = Vehicle.objects.all()
    serializer_class = VehiclesSerializer

class StarshipsViewSet(viewsets.ModelViewSet):
    """SHOW TO STARSHIPS"""
    queryset = Starship.objects.all()
    serializer_class = StarShipsSerializer

class SpeciesViewSet(viewsets.ModelViewSet):
    """SHOW TO SPECIES"""
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer




def init(request):
    if request.method == 'GET':
        exec()
        isLoad = {'isLoad':'OK'}
        return JsonResponse(isLoad)