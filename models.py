from django.db import models

# Create your models here.


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
    image = models.ImageField(upload_to="uploads/images/", blank=False)
    created = models.DateTimeField(blank=False)

    class Meta:
        ordering = ("-created",)
