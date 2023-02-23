from django.contrib import admin

from userapp.models import Order, Storage,Chat

admin.site.register(Order)
admin.site.register(Storage)
admin.site.register(Chat)
