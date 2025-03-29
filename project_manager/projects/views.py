from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from .models import Project
from .serializers import ProjectSerializer
from django.shortcuts import render

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]


def liste_projets(request):
    projets = Project.objects.prefetch_related("taches").all()
    return render(request, "liste_projets.html", {"projets": projets})
