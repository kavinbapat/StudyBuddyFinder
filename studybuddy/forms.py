from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django import forms

from .models import Session


# """/***************************************************************************************
# *  REFERENCES
# *  Repository name: django-bootstrap-datepicker-plus
# *  Author: monim67
# *  Date: November 27, 2022
# *  URL: https://github.com/monim67/django-bootstrap-datepicker-plus
# *
# *  Description: Utilized to create date time picker for selecting study session time
# *
# ***************************************************************************************/"""

class StudySessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ["sessions"]
        widgets = {"sessions": DateTimePickerInput()}
