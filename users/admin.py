from django.contrib import admin
from users.models import Profile, Skill

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_filter = ("created_at",)
    list_display = ("name", "email")

class SkillAdmin(admin.ModelAdmin):
    list_filter = ("owner",)
    list_display = ("name", "owner")

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skill, SkillAdmin)
