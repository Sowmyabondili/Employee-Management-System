from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'department', 'designation', 'salary', 'status', 'date_joined']
    list_filter = ['department', 'status', 'date_joined']
    search_fields = ['first_name', 'last_name', 'email', 'designation']
    ordering = ['-created_at']
    list_per_page = 20
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'photo', 'address')
        }),
        ('Job Details', {
            'fields': ('department', 'designation', 'salary', 'date_joined', 'status')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
