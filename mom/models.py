from django.db import models
from django.urls import reverse
from django.shortcuts import render

# Create your models here.


class DogHome(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Dog(models.Model):
    home = models.ForeignKey(DogHome, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    date_of_birth = models.DateTimeField()
    arrival_date = models.DateTimeField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dog_detail', args=[str(self.id)])
