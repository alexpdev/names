from django.contrib import admin

# Register your models here.
from pages.models import Name

class NameAdmin(admin.ModelAdmin):
    list_display = ('name','sex','amount','year')


admin.site.register(Name,NameAdmin)
