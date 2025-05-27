from django.urls import path
from rest_framework.routers import DefaultRouter
from clients.api import ClientViewSet
from affaires.api import AffaireViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'affaires', AffaireViewSet)

urlpatterns = router.urls + [
    # Endpoints supplémentaires
]