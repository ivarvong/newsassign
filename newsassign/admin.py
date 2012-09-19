from django.contrib import admin
from newsassign.models import Story
from newsassign.models import Assignment

class AssignmentInline(admin.StackedInline):
  model = Assignment
  extra = 1

class StoryAdmin(admin.ModelAdmin):
  fields = ['slug', 'description', 'created_date']
  inlines = [AssignmentInline]
  list_display = ['slug', 'description', 'created_date', 'was_created_recently']
  #list_filter = ['created_date']
  search_fields = ['slug', 'description']
  #date_hierarchy = 'created_date'
  
admin.site.register(Story, StoryAdmin)

class AssignmentAdmin(admin.ModelAdmin):
  list_display = ['story', 'slug', 'description', 'was_created_recently']

admin.site.register(Assignment, AssignmentAdmin)
