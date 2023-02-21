from django.forms import ModelForm
from projects.models import Project, Review
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ["owner","created_at", "id", "vote_total", "vote_ratio"]
        widgets = {
            'tags': forms.CheckboxSelectMultiple()
        }
    
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            
        #self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'Add Title'})
        #self.fields['description'].widget.attrs.update({'class': 'input', 'placeholder': 'Add Description'})

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']
        
        labels = {
            'value': 'Place your vote',
            'body': 'Add a comment with your vote'
        }
        
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})