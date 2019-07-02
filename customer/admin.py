from django.contrib import admin

from customer.models import User, Customer, Location

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Location)