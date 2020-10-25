from django.contrib import admin

from dictionary import models


@admin.register(models.State)
class StateAdmin(admin.ModelAdmin):
	pass

@admin.register(models.Mark)
class MarkAdmin(admin.ModelAdmin):
	pass
	
@admin.register(models.Model)
class ModelAdmin(admin.ModelAdmin):
	pass

@admin.register(models.Color)
class ColorAdmin(admin.ModelAdmin):
	pass

