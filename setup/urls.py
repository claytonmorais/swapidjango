from django.contrib import admin
from django.urls import path, include
from api.views import FilmsViewSet,PlanetsViewSet,PeoplesViewSet,VehiclesViewSet,StarshipsViewSet,SpeciesViewSet, init
from rest_framework import routers

router = routers.DefaultRouter()
router.register('films', FilmsViewSet, basename='Films')
router.register('planets', PlanetsViewSet, basename='Planets')
router.register('peoples', PeoplesViewSet, basename='Peoples')
router.register('vehicles', VehiclesViewSet, basename='Vehicles')
router.register('starships', StarshipsViewSet, basename='Starships')
router.register('species', SpeciesViewSet, basename='Species')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sw-django/', include(router.urls) ),
    path('init/', init),
    path('prometheus/', include('django_prometheus.urls')),
    path('swapi/health/', include('health_check.urls')),
]
