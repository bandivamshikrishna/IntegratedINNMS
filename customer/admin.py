from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['id','user','gender','profile_pic']

@admin.register(CustomerRoom)
class CustomerRoomAdmin(admin.ModelAdmin):
    list_display=['id','customer','room','price']


@admin.register(CustomerRoomCustomization)
class CustomizationRoomCustomizationAdmin(admin.ModelAdmin):
    list_display=['id','left','right','top','front']
