from django import forms
from .models import Cell_Report

class CellReportForm(forms.ModelForm):
    class Meta:
        model = Cell_Report
        fields = (
            'report', 
            'description',
        )