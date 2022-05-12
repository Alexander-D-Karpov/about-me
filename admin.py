from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(Link)
class RateAdmin(admin.ModelAdmin):
    list_display = ("order", "name", "link")
    list_filter = ("order",)


@admin.register(Stack)
class RateAdmin(admin.ModelAdmin):
    list_display = ("order", "name", "link")
    list_filter = ("order",)


admin.site.register(Project)
