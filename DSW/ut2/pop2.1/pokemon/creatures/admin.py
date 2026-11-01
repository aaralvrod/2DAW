from django.contrib import admin

# Register your models here.
from .models import Creature


@admin.register(Creature)
class CreatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'name')
