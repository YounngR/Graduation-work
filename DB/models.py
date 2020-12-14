from django.db import models
from datetime import datetime

# Create your models here.
class Hospital(models.Model):
    h_Name = models.CharField(max_length=100, null=True, blank=True)
    h_Grade = models.CharField(max_length=30, null=True, blank=True)
    h_Latitude = models.CharField(max_length=50, null=True, blank=True)
    h_Longitute = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.h_Name


class Medicine(models.Model):
    m_Name = models.CharField(max_length=50, null=True, blank=True)
    m_Code = models.CharField(max_length=50, null=True, blank=True)
    m_Efficacy = models.CharField(max_length=1000, null=True, blank=True)
    m_Side_Effect = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.m_Name

class image(models.Model):
    sample = models.ImageField()
    date    = models.DateField(auto_now_add=True, null=True)
