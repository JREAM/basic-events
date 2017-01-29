from django import forms
from .models import Event


class CreateForm(forms.ModelForm):

    class Meta:
        model = Event
        #fields = []

    def clean_date(self):
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        if start_date > end_date:
            self.add_error(self.start_date, 'The start date must come before end date.')

