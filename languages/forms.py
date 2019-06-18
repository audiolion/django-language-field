from django import forms

class LanguageField(forms.ChoiceField):
    """
    A language field for Django forms.
    """
    def __init__(self, *args, **kwargs):
        from .languages import LANGUAGES
        defaults = {'choices': LANGUAGES}
        defaults.update(kwargs)
        super().__init__(*args, **defaults)