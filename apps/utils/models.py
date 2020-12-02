from random import randint

from django.contrib.gis.db import models

from apps.utils.managers import Osw4lModelModelManager


class ModelBase(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    archived = models.BooleanField(default=False)
    objects = Osw4lModelModelManager()

    class Meta:
        abstract = True


class NameModelBase(ModelBase):
    name = models.CharField(
        max_length=50,
        unique=True
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


