from django.db import models

# Create your models here.

class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False, unique=True)

    def __str__(self):
        return "<Publisher object: {0}>".format(self.name)

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False, unique=True)
    publisher = models.ForeignKey(to="Publisher")

    def __str__(self):
        return "<Book object: {0}>".format(self.name)

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False, unique=True)
    book = models.ManyToManyField(to="Book")

    def __str__(self):
        return "<Author object: {0}>".format(self.name)
