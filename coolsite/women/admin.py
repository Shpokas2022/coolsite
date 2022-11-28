from django.contrib import admin
from . import models

class WomenAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'photo')


admin.site.register(models.Women, WomenAdmin)
