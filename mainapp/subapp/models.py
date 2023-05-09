from django.db import models

# Create your models here.
class Region(models.Model):
    name =models.CharField(max_length=270)
    city = models.CharField(max_length=270)

    def __str__(self):
        return self.name
    
    
class Person(models.Model):
    id = models.IntegerField(unique=True,primary_key=True)
    name = models.CharField(max_length=270)
    email = models.EmailField(max_length=270)
    age = models.IntegerField()
    country = models.ForeignKey( Region,null=True,blank=True, on_delete= models.CASCADE, related_name= 'country')

