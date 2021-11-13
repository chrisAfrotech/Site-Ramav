from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
#from api_rest import api_views  
from api_rest import vues_api


router = DefaultRouter()
router.register('description', vues_api.DescriptionViewSet, basename="description")
router.register('membre', vues_api.MembreViewSet, basename="membre")
router.register('service', vues_api.ServiceViewSet, basename="service")
router.register('projet', vues_api.ProjectViewSet, basename="projet")
router.register('contact', vues_api.ContactViewSet, basename="contact")
router.register('slide', vues_api.SlideViewSet, basename="slide")

urlpatterns = []

urlpatterns += router.urls
