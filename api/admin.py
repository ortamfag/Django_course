from django.contrib import admin
from .models import Student, Project, Group
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin

@admin.register(Student)
class StudentAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    class Meta:
        proxy = True

@admin.register(Project)
class ProjectAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    class Meta:
        proxy = True

@admin.register(Group)
class GroupAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    class Meta:
        proxy = True
