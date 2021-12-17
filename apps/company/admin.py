from django.contrib import admin

from apps.company.models import CompanyModel, DepartmentModel, WorkingModel


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)


class WorkingAdmin(admin.ModelAdmin):
    list_display = ('user', 'working_type', 'starting_time', 'ending_time')


admin.site.register(CompanyModel, CompanyAdmin)
admin.site.register(DepartmentModel, DepartmentAdmin)
admin.site.register(WorkingModel, WorkingAdmin)
