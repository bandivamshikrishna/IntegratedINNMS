from turtle import right
from django.db import models
from django.contrib.auth.models import User
from core.models import Room
from designer.models import RoomCustomization,Designer


# Create your models here.
gender_choices=(('male','Male'),('female','Female'))
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    gender=models.CharField(max_length=20,choices=gender_choices)
    profile_pic=models.ImageField(upload_to='profile_pic/customer/')
    room_number=models.PositiveIntegerField(null=True)



duration_choices=(('3 months','3 Months'),('6 months','6 Months'),('9 months','9 Months'),('12 months','12 Months'),('more than 1 year','More than 1 Year'))
occupation_choices=(('student','Student'),('empolyee','Empolyee'))
caste_choices=(('BC-A','BC-A'),('BC-B','BC-B'),('BC-C','BC-C'),('BC-D','BC-D'),('OC','OC'),('SC/ST','SC/ST'),('OTHERS','OTHERS'))
class HostelCustomer(models.Model):
    customer=models.OneToOneField(Customer,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE,null=True)
    room_number=models.PositiveIntegerField(null=True)
    date_of_birth=models.DateField()
    age=models.PositiveIntegerField()
    check_in=models.DateField()
    duration=models.CharField(max_length=40,choices=duration_choices)
    occupation=models.CharField(max_length=100,choices=occupation_choices)
    work_place=models.CharField(max_length=200)
    profession=models.CharField(max_length=400)
    caste=models.CharField(max_length=100,choices=caste_choices)
    contact_number=models.PositiveIntegerField()
    guardian_name=models.CharField(max_length=400)
    guardian_relation=models.CharField(max_length=400)
    guardian_contact_number=models.PositiveIntegerField()
    emergency_contact_number=models.PositiveIntegerField()
    permanent_address=models.TextField()
    city=models.CharField(max_length=400)
    state=models.CharField(max_length=400)
    pincode=models.PositiveIntegerField()
    total_fees=models.PositiveIntegerField(null=True)
    admin_status=models.BooleanField(default=False)


class CustomerRoom(models.Model):
    room=models.OneToOneField(RoomCustomization,on_delete=models.CASCADE)
    customer=models.OneToOneField(Customer,on_delete=models.CASCADE)
    price=models.PositiveIntegerField(null=True,blank=True)
    designer=models.ForeignKey(Designer,on_delete=models.CASCADE,null=True)


class CustomerRoomCustomization(models.Model):
    customer=models.OneToOneField(Customer,on_delete=models.CASCADE)
    left=models.ImageField(upload_to='rooms/')
    right=models.ImageField(upload_to='rooms/')
    top=models.ImageField(upload_to='rooms/')
    bottom=models.ImageField(upload_to='rooms/',null=True)
    front=models.ImageField(upload_to='rooms/')
    back=models.ImageField(upload_to='rooms/',null=True)
    designer_status=models.BooleanField(default=False)
    designer=models.ForeignKey(Designer,on_delete=models.CASCADE,null=True)
    price=models.PositiveIntegerField(null=True)
    updated_room=models.BooleanField(default=False,null=True)



class CustomerComplaint(models.Model):
    hostel_customer=models.ForeignKey(HostelCustomer,on_delete=models.CASCADE)
    complaint=models.TextField()