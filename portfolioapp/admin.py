from django.contrib import admin
from . models import Aboutme, Count, Skill,Interest,Contact


#List display
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


# Register your models here.
admin.site.register(Aboutme,AboutmeAdmin)
admin.site.register(Count,CountAdmin)
admin.site.register(Skill,SkillAdmin)
admin.site.register(Interest,InterestAdmin)
admin.site.register(Contact,ContactAdmin)

