from django.contrib import admin

from .models import System
# Register your models here.





class SystemAdmin(admin.ModelAdmin):

    list_display = ("name", "layer")
    list_filter = ["layer", "category", "service", "name"]
    filter_horizontal = ["connect_to", "connect_from", "parent"]
    search_fields = ["name", "memo"]

    # fieldssets = 

admin.site.register(System, SystemAdmin)