from django.contrib import admin
from .models import OpenlabModel

# Register your models here.


class OpenlabAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(OpenlabModel, OpenlabAdmin)
