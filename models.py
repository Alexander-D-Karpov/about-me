from django.db import models

# Create your models here.
from django.urls import reverse


class Link(models.Model):
    order = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)


class Stack(models.Model):
    order = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)


class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    md = models.TextField(blank=True)
    image = models.ImageField(upload_to="uploads/images/", blank=False)
    created = models.DateTimeField(blank=False)
    last_updated = models.DateTimeField(blank=True, null=True)
    source_link = models.URLField(blank=True)
    view_link = models.URLField(blank=True)

    def get_absolute_url(self):
        return reverse("project", kwargs={"id": self.id})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-last_updated",)
