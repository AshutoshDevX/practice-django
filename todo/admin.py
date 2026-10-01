from django.contrib import admin
from .models import Task
# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = '__all__'
    list_filter = ('completed_at', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at')