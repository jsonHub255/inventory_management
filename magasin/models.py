from django.db import models

# Create your models here.
class Designation(models.Model):

    name = models.CharField(max_length=50)
    ref = models.CharField(max_length=50)
    qty = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name} {self.ref} {self.qty}"


class Engin(models.Model):
    
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    desi = models.ForeignKey(Designation, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.code}"