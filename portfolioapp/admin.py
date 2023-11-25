from django.contrib import admin
from . models import Aboutme, Count, Skill, Interest, Contact
from . models import Summary, Degree, Department, Education, Professional_Experience, Professional_Traning

# List display


class SummaryAdmin(admin.ModelAdmin):
    list_display = ('summery_details',)


class DegreeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)


class EducationAdmin(admin.ModelAdmin):
    list_display = ('degrees', 'department', 'institute', 'gread_point')


class Professional_ExperienceAdmin(admin.ModelAdmin):
    list_display = ('designation', 'company_name',
                    'joining_date', 'resign_date')


class AboutmeAdmin(admin.ModelAdmin):
    list_display = ('name', 'github', 'degree', 'email', 'freelance_status', )


class CountAdmin(admin.ModelAdmin):
    list_display = ('what_count', 'count_number', 'icon',)


class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'progress',)


class InterestAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')


class Professional_TraningAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_duration', 'course_institute')


# Register your models here.
admin.site.register(Aboutme, AboutmeAdmin)
admin.site.register(Count, CountAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Summary, SummaryAdmin)
admin.site.register(Degree, DegreeAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Professional_Experience, Professional_ExperienceAdmin)
admin.site.register( Professional_Traning,Professional_TraningAdmin)
