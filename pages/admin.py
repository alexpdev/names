from django.contrib import admin
from pages.models import Name

# Register your models here.

class NameAdmin(admin.ModelAdmin):
    list_display = ('name','sex','amount','year')




admin.site.register(Name,NameAdmin)
