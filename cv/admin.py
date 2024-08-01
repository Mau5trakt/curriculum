from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, PersonalInformation, WorkExperience, Language, Course, ProgrammingExperience, Achievement, Additional
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['id', 'username', 'fullname', 'email', 'birthday', 'phone_number' ]
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info',
         {'fields': ('fullname', 'email', 'birthday', 'phone_number')}),
         ('Permissions',
          {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates',
         {'fields': ('last_login', 'date_joined')}),

    )


@admin.register(PersonalInformation)
class PersonalInformationAdmin(admin.ModelAdmin):
    list_display = ['user', 'date',  'information']


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ['user', 'from_date', 'to_date', 'position', 'description']


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'level', 'where']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'from_date', 'to_date']


@admin.register(ProgrammingExperience)
class ProgrammingExperienceAdmin(admin.ModelAdmin):
    list_display = ['user', 'ability', 'h_type']


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'link']


@admin.register(Additional)
class AdditionalAdmin(admin.ModelAdmin):
    list_display = ['user', 'from_date', 'to_date', 'title']
