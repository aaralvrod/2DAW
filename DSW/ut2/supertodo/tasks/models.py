from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=256, blank=True)
    slug = models.SlugField(max_length=256, unique=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
