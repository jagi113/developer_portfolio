from django.forms import ModelForm
from projects.models import Project
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ["created_at", "id", "vote_total", "vote_ratio"]