from django import forms
from languages.forms import LanguageField

class TestForm(forms.Form):
    language = LanguageField()
