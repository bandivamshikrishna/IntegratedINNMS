from django.db import models
from django.contrib.auth.models import User


# Create your models here.
gender_choices=(('male','Male'),('female','Female'))
class Designer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    gender=models.CharField(max_length=20,choices=gender_choices)
    profile_pic=models.ImageField(upload_to='profile_pic/designer/')
    approved=models.BooleanField(default=False,null=True)
    resume=models.FileField(upload_to='resumes/',null=True)



class RoomCustomization(models.Model):
    designer=models.ForeignKey(Designer,on_delete=models.CASCADE,null=True)
    left=models.ImageField(upload_to='rooms/')
    right=models.ImageField(upload_to='rooms/')
    top=models.ImageField(upload_to='rooms/')
    bottom=models.ImageField(upload_to='rooms/',null=True)
    front=models.ImageField(upload_to='rooms/')
    back=models.ImageField(upload_to='rooms/',null=True)
    price=models.PositiveIntegerField(null=True)
    theme=models.CharField(max_length=400,null=True)