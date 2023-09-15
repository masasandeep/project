from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True,max_length=254)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
class MainDivisions(models.Model):
    name = models.CharField( max_length=50,null=True)
    def __str__(self) -> str:
        return self.name
class Testcategories(models.Model):
    division = models.ForeignKey(MainDivisions, verbose_name=("division"), on_delete=models.CASCADE,null=True)
    name = models.CharField( max_length=50,null=True)
    n1 = models.CharField(max_length=50,blank=True,null=True)
    n2 = models.CharField(max_length=50,blank=True,null=True)
    n3 = models.CharField(max_length=50,blank=True,null=True)
    n4 = models.CharField(max_length=50,blank=True,null=True)
    n5 = models.CharField(max_length=50,blank=True,null=True)
    n6 = models.CharField(max_length=50,blank=True,null=True)
    def __str__(self):
        return self.name
class TestResults(models.Model):
    category = models.ForeignKey(Testcategories, verbose_name=("category"), on_delete=models.SET_NULL,null=True)
    n1 = models.CharField(max_length=50,blank=True,null=True,default="Null")
    n2 = models.CharField(max_length=50,blank=True,null=True,default="Null")
    n3 = models.CharField(max_length=50,blank=True,null=True,default="Null")
    n4 = models.CharField(max_length=50,blank=True,null=True,default="Null")
    n5 = models.CharField(max_length=50,blank=True,null=True,default="Null")
    n6 = models.CharField(max_length=50,blank=True,null=True,default="Null")
    def __str__(self):
        return f'{self.category}'  
class Reports(models.Model):
    Testname = models.CharField(max_length=50,null=True)
    image = models.FileField()
    def __str__(self):
        return self.Testname