from datetime import datetime

from django import forms

from apps.company.models import WorkingModel


class WorkingForm(forms.ModelForm):
    WORKING_TYPES = [
        ('sh', 'shift'),
        ('over', 'overtime shift'),
        ('rm', 'remote')]

    working_type = forms.ChoiceField(choices=WORKING_TYPES, label='Çalışma Tipi')
    starting_time = forms.DateTimeField(initial=datetime.now(), label='Başlangıç Zamanı')
    ending_time = forms.DateTimeField(initial=datetime.now(), label='Bitiş Zamanı')

    class Meta:
        model = WorkingModel
        fields = ['working_type', 'starting_time', 'ending_time', ]
