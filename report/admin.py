from django.contrib import admin

from .models import Cell_Report, Member


class CellReportAdmin(admin.ModelAdmin):
    list_display = (
        'report',
        'description',
        'created_dt',
        'created_by',
        'updated_dt',
        'updated_by',
    )
admin.site.register(Cell_Report, CellReportAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'gender',
        'date_of_birth',
        'cell_group',
        'status',
        'baptism',
        'created_dt',
        'created_by',
        'updated_dt',
        'updated_by',
    )
admin.site.register(Member, MemberAdmin)
