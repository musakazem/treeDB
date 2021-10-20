from django.db import models

# Create your models here.




class MainDb(models.Model):
    number_plate = models.CharField(max_length=50, blank=True, null=True)
    age = models.CharField(max_length=50, blank=True, null=True)
    trunk_circumference = models.IntegerField(blank=True, null=True)
    year_planted = models.CharField(max_length=50, blank=True, null=True)
    health = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    sector = models.CharField(max_length=50, blank=True, null=True)
    type = models.ForeignKey('TypeDb', models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'main_db'


class TypeDb(models.Model):
    id = models.IntegerField(primary_key=True)
    tree_type = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    fruit_bearing = models.CharField(max_length=50, blank=True, null=True)
    season = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'type_db'

