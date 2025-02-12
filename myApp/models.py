from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Services(models.Model):
    image= models.ImageField(upload_to='image/',blank=True,null=True)
    title= models.CharField(max_length=200,blank=True,null=True)
    sub_title=models.CharField(max_length=200,blank=True,null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user',blank=True,null=True)


    def __str__(self):
        return self.title
    

class SliderOne(models.Model):
    image= models.ImageField(upload_to='sliderone/',blank=True,null=True)
    title= models.CharField(max_length=200,blank=True,null=True)
    sub_title=models.CharField(max_length=200,blank=True,null=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE,related_name='sliderone',blank=True,null=True)
    

    def __str__(self):
        return self.title
    

class SliderTwo(models.Model):
    image= models.ImageField(upload_to='sliderTwo/',blank=True,null=True)
    name= models.CharField(max_length=100,blank=True,null=True)
    title= models.CharField(max_length=200,blank=True,null=True)
    sub_title=models.CharField(max_length=200,blank=True,null=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE,related_name='sliderTwo',blank=True,null=True)
    

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name=models.CharField(max_length=50,blank=True, null= True)
    subject=models.CharField(max_length=50,blank=True,null=True)
    phone=models.CharField(max_length=11,blank=True,null=True)
    email=models.EmailField(max_length=50,unique=True,blank=True,null=True)
    message=models.TextField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.name
    
    
