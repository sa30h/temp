from django.db import models

# Create your models here.
class Temp(models.Model):
    name=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    date=models.DateField()
    temp_f=models.CharField(max_length=50)

    def __str__(self):
        return str(self.country+" "+str(self.date))