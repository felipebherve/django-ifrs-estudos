from django.db import models

class Companhia(models.TextChoices):
    OO = 'OO', 'SkyWest Airlines'
    DL = 'DL', 'Delta Airlines'
    UA = 'UA', 'United Airlines'
    AA = 'AA', 'American Airlines'
    WN = 'WN', 'Southwest Airlines'