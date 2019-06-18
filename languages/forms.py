from django import forms

class LanguageField(forms.ChoiceField):
    """
    A language field for Django forms.
    """
    def __init__(self, *args, **kwargs):
        defaults = {} # {'choices': }
        defaults.update(kwargs)
        super().__init__(*args, *args, **defaults)