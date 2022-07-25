from django.db import models

# Create your models here.
class Room(models.Model):
    room_pic=models.ImageField(upload_to='core/')
    room_type=models.CharField(max_length=400)
    room_fees=models.PositiveIntegerField()



class WorkerDetails(models.Model):
    full_name=models.CharField(max_length=400)
    profession=models.CharField(max_length=400)
    contact_number=models.PositiveIntegerField()
    salary=models.PositiveIntegerField()
    profile_pic=models.ImageField(upload_to='core/')


class Menu(models.Model):
    day=models.CharField(max_length=100)
    breakfast=models.CharField(max_length=1000)
    lunch=models.CharField(max_length=1000)
    dinner=models.CharField(max_length=1000)


class Rules(models.Model):
    rules=models.TextField()

   