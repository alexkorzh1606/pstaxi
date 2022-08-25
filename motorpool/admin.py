from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    pass
