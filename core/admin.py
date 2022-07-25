from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display=['id','room_pic','room_type','room_fees']



@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display=['day','breakfast','lunch','dinner']


@admin.register(Rules)
class RulesAdmin(admin.ModelAdmin):
    list_display=['rules']