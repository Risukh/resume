from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.profile)
admin.site.register(models.skills)
admin.site.register(models.Education)