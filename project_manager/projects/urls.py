from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet,liste_projets

router = DefaultRouter()
router.register(r"projects", ProjectViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("projets/", liste_projets, name="liste_projets"),
]
