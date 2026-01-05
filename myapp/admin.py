from django.contrib import admin
from .models import Mycontact
# Register your models here.
@admin.register(Mycontact)
class MycontactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'pub_date']
    search_fields = ['name', 'email', 'phone']