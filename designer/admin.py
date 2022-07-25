from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(RoomCustomization)
class RoomCustomizationAdmin(admin.ModelAdmin):
    list_display=['id','left','right','top','front']