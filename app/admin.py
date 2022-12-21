from django.contrib import admin

from app import models

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Tag)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Question)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Answer)
class ProfileAdmin(admin.ModelAdmin):
    pass
