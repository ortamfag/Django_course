from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import Group
from .models import User


@admin.register(User)
class UserAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    class Meta:
        proxy = True

admin.site.unregister(Group)
