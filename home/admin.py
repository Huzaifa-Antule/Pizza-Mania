from django.contrib import admin
from home.models import Contact , Order

class contactFilter(admin.ModelAdmin):
    list_display =['name','email','number','desc']

class orderFilter(admin.ModelAdmin):
    list_display =['name','number','number1','Address','Onion_pizza','Sweet_Corn_pizza','total_bill']

# Register your models here.
admin.site.register(Contact,contactFilter)
admin.site.register(Order,orderFilter)
