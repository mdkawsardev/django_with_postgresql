from django.contrib import admin
from .models import Mycontact, Myusers, Customers
# Register your models here.
@admin.register(Mycontact)
class MycontactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'pub_date']
    search_fields = ['name', 'email', 'phone']

@admin.register(Myusers)
class amarUser(admin.ModelAdmin):
    list_display = ['users', 'email']
@admin.register(Customers)
class amarCustomer(admin.ModelAdmin):
    list_display = ['customer', 'phn']