from django import forms

class WorkEventForm(forms.Form):
    start_time = forms.TimeField(required=True)
    end_time = forms.TimeField(required=True)
    start_date = forms.DateField(required=True)
    comments = forms.TextField()
    on_campus = forms.BooleanField(required=True)
