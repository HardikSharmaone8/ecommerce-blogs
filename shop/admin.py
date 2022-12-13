from django.contrib import admin
from .models import Items, Contacts, Checkout, Tracker
# Register your models here.

admin.site.register(Items)
admin.site.register(Contacts)
admin.site.register(Checkout)
admin.site.register(Tracker)