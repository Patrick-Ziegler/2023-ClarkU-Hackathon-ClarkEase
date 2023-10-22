from django.db import models

# Create your models here.

class buildingData(models.Model):
    buildingName = models.CharField(max_length=64)
    hasElevator = models.BooleanField()
    isElevatorWorking = models.BooleanField()
    hasRamps = models.BooleanField()
    numEntrances = models.PositiveSmallIntegerField()
    numMotorizedEntrances = models.PositiveSmallIntegerField()
    
    
    def __str__(self):
        return self.buildingName