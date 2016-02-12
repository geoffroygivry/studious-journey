from django.contrib import admin

# Register your models here.

from .models import ChoreList, Chore

class ChoreInLine(admin.TabularInline):
  model = Chore
  extra = 0

class ChoreListAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {'fields': ['name']}),
    ('Date Infos', {'fields':['due_date'], 'classes' : ['collapse']})
  ]
  inlines = [ChoreInLine]

admin.site.register(ChoreList, ChoreListAdmin)