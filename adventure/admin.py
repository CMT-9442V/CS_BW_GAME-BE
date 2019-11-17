from django.contrib import admin

from .models import Room, Player

admin.site.site_header = 'Adventure Game'
admin.site.site_title='Adventure Game Administration'

admin.site.register(Room)
admin.site.register(Player)
# Register your models here.
