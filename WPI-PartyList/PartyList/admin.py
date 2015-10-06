from django.contrib import admin
from PartyList.models import Party, Guest, PartyGuest

# Register your models here.
admin.site.register(Party)
admin.site.register(Guest)
admin.site.register(PartyGuest)