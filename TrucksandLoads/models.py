from __future__ import unicode_literals

from django.db import models

class Trucks(models.Model):
    truck_company_name=models.CharField(max_length=50)
    truck_type=models.CharField(max_length=50)
    start_point=models.CharField(max_length=50)
    end_point=models.CharField(max_length=50)

    class Meta:
        ordering = ('truck_company_name',)

class Load(models.Model):
    TYPE_CHOICES=(
       ('F', 'Full'),
       ('P', 'Partial')
     )
    type = models.CharField(max_length=6, choices=TYPE_CHOICES, default='Full')
    start_point = models.CharField(max_length=50)
    end_point = models.CharField(max_length=50)


# Create your models here.
