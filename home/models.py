from django.db import models

# Create your models here.
class WorkCV(models.Model):
    nameCV = models.CharField(max_length=50)
    images = models.ImageField(upload_to='work/')
    discriptions = models.CharField(max_length=255)

    def __str__(self) :
        return self.nameCV
    

