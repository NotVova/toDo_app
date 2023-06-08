from django.contrib import admin

from .models import Objective, ObjectiveValue

admin.site.register(ObjectiveValue)


@admin.register(Objective)
class ObjectiveAdmin(admin.ModelAdmin):
    list_display = ("name", )
    fields = ("name", "objective", "value", "completed", )
    search_fields = ("name", "objective", )
