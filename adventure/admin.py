from django.contrib import admin

from .models import Channel, Player

admin.site.site_header = 'Adventure Game'
admin.site.site_title='Adventure Game Administration'

admin.site.register(Channel)
admin.site.register(Player)
# Register your models here.
