from django.contrib import admin
from .models import Team, Project, Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "deadline", "assignee", "project")
    list_filter = ("status", "project", "tags")
    search_fields = ("title", "description")


admin.site.register(Team)
admin.site.register(Project)
admin.site.register(Tag)
