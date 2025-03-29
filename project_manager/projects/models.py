from django.db import models
from users.models import User

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    members = models.ManyToManyField(User, related_name="project_members")

    def __str__(self):
        return self.name
