from django.db import models

# Create your models here.

class buildingData(models.Model):
    buildingName = models.CharField(max_length=64)
    hasElevator = models.CharField(max_length=64)
    isElevatorWorking = models.CharField(max_length=64)
    hasRamps = models.CharField(max_length=64)
    numEntrances = models.PositiveSmallIntegerField(null=True)
    numMotorizedEntrances = models.PositiveSmallIntegerField(null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    
    
    def __str__(self):
        return self.buildingName