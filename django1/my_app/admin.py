from django.contrib import admin

# Register your models here.

from my_app.models import Currency, Rates

class RatesInline(admin.TabularInline): #or StackedInline
    readonly_fields = ('time_since_last_update',)
    model = Rates #The model connected
    extra = 3 #enough space for three extra Rates

class CurrencyAdmin(admin.ModelAdmin):
    fields = ['identifier','long_name','date_added']
    inlines=[RatesInline] #Connection to Rates
    list_display = ('identifier','long_name','date_added')
    list_filter = ['long_name']
    search_field =['identifier']

admin.site.register(Currency, CurrencyAdmin)