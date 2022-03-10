from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Teeth_Model(models.Model):

    name = models.CharField(max_length=50, null=True, blank= True)
    phone_number = models.IntegerField(default=0)
    email = models.EmailField(null=True, max_length=255)
    image = models.ImageField(upload_to = 'images/')
    detected_image = models.ImageField(upload_to = 'imagesresult/')
    teeth_score = models.TextField()

    class Meta:
        db_table = 'teeth'

    def delete(self,*args,**kwargs):
        self.image.delete()
        self.detected_img.delete()
        super().delete(*args,**kwargs)
