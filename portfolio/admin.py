from django.contrib import admin
from .models import Profile, Project, Skill, Experience, ContactMessage


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'role', 'available_for_work']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order']
    list_editable = ['order', 'proficiency']
    list_filter = ['category']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_featured', 'order', 'created_at']
    list_editable = ['is_featured', 'order']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['technologies']
    search_fields = ['title', 'description']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['role', 'company', 'type', 'start_date', 'end_date', 'order']
    list_editable = ['order']
    list_filter = ['type']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'sent_at', 'is_read']
    list_editable = ['is_read']
    readonly_fields = ['name', 'email', 'subject', 'message', 'sent_at']
    list_filter = ['is_read']
