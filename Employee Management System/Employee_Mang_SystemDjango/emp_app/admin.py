from django.contrib import admin
from .models import Employee, Roles, Department
# Register your models here.

@admin.register(Employee, Roles, Department)
class UniversalAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]
