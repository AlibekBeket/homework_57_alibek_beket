from django import forms
from django.core.exceptions import ValidationError

from issue_tracker.models import Issue

from issue_tracker.models import Type, Status


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('summary', 'description', 'status', 'type')
        labels = {
            'summary': 'Краткое описание',
            'description': 'Описание',
            'status': 'Статус',
            'type': 'Тип'
        }

    def clean_summary(self):
        summary = self.cleaned_data.get('summary')
        if len(summary) < 3:
            raise ValidationError('Краткое описание не сожет быть пустым или состоять из менее чем 2 символов')
        return summary
