from django.contrib import admin
from .models import Project_title,Project_items,Skill,Skill_tools
# Register your models here.
admin.site.register(Project_title)
@admin.register(Project_items)
class Project_itemsAdmin(admin.ModelAdmin):
    list_display=['id','image', 'heading','desc','language_used','url']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display=['id','icon', 'name','desc','percent']

@admin.register(Skill_tools)
class Skill_toolsAdmin(admin.ModelAdmin):
    list_display=['id','icon', 'name']