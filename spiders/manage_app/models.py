from django.db import models

# Create your models here.
class TZhilianzhaopin(models.Model):
    position = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    salary = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    experience = models.CharField(max_length=255, blank=True, null=True)
    education = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    requirement = models.TextField(blank=True, null=True)
    amount_need = models.CharField(max_length=255, blank=True, null=True)
    amount_total = models.CharField(max_length=255, blank=True, null=True)
    business = models.CharField(max_length=255, blank=True, null=True)
    nature = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    welfare = models.TextField(blank=True, null=True)
    situation = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 't_zhilianzhaopin'
