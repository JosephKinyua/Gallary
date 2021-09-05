from django.db import models

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length=200)

    def saveLocation(self):
        self.save()

    @classmethod
    def deleteLocation(cls, id):
        cls.objects.filter(id=id).delete()

    
    @classmethod
    def updateLocation(cls, id, locaUpdate):
        cls.objects.filter(id=id).update(location=locaUpdate)

    def __str__(self):
        return self.location
