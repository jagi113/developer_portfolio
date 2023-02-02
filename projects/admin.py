from django.contrib import admin
from projects.models import Project, Review, Tag

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_filter = ("created_at","vote_ratio")
    list_display = ("title", )
    
class ReviewAdmin(admin.ModelAdmin):
    list_filter = ("created_at","project")


admin.site.register(Project, ProjectAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Tag)