from django.contrib import admin
from users.models import Profile, Skill, Message

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_filter = ("created_at",)
    list_display = ("username", "name", "email")

class SkillAdmin(admin.ModelAdmin):
    list_filter = ("owner",)
    list_display = ("name", "owner")
    
class MessageAdmin(admin.ModelAdmin):
    list_filter = ("sender", "is_read" )
    list_display = ("__str__", "name", "recipient", "subject", "is_read", "created_at")

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Message, MessageAdmin)
