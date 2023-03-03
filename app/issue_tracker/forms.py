from django import forms
from django.core.exceptions import ValidationError

from issue_tracker.models import Issue

from issue_tracker.models import Type, Status


class IssueForm(forms.ModelForm):
    type = forms.ModelChoiceField(required=True, queryset=Type.objects.all(), label='Type')
    status = forms.ModelChoiceField(required=True, queryset=Status.objects.all(), label='Status')

    class Meta:
        model = Issue
        fields = ('summary', 'description')
        labels = {
            'summary': 'Краткое описание',
            'description': 'Описание'
        }

    def clean_summary(self):
        summary = self.cleaned_data.get('summary')
        if len(summary) < 3:
            raise ValidationError('Краткое описание не сожет быть пустым или состоять из менее чем 2 символов')
        return summary
