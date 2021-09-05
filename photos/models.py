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
class Image(models.Model):
    image = models.ImageField(upload_to='photos')
    image_name =  models.CharField(max_length=200)
    image_desc = models.TextField()
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE, default=None)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    date_upload = models.DateTimeField(auto_now_add=True)


    def save_image(self):
        self.save()

    @classmethod
    def delete_image(cls, id):
        cls.objects.filter(id=id).delete()

    @classmethod
    def update_image(cls, id, imagechange):
        cls.objects.filter(id = id).update(image = imagechange)



