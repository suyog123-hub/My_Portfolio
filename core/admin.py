from django.contrib import admin
from .models import Project_title, Project_items, Skill, Skill_tools, Contact, Testinomial, skill_title, skill_items

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'subject', 'phone']

@admin.register(Project_title)
class ProjectTitleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

@admin.register(Project_items)
class Project_itemsAdmin(admin.ModelAdmin):
    list_display = ['id', 'heading', 'category', 'language_used', 'url']

@admin.register(skill_title)
class SkillTitleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

@admin.register(skill_items)
class SkillItemsAdmin(admin.ModelAdmin):
    list_display = ['id', 'heading', 'category', 'language_used']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'icon', 'name', 'desc', 'percent']

@admin.register(Skill_tools)
class Skill_toolsAdmin(admin.ModelAdmin):
    list_display = ['id', 'icon', 'name']

@admin.register(Testinomial)
class TestinomialAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'role', 'company', 'is_active']
    list_filter = ['is_active']
