from django import forms
from django.core.cache import caches

sorted_languages = None
def _get_sorted_languages():
    from .languages import LANGUAGES
    global sorted_languages
    if sorted_languages:
        return sorted_languages
    sorted_languages = sorted(LANGUAGES, key=lambda p: p[1])
    return sorted_languages

class _LanguageWidget(forms.Select):
    def render(self, name, value, attrs=None, renderer=None):
        cache = caches['default']
        result = cache.get(value or '')
        if result is not None:
            return result
        result = super().render(name, value, attrs, renderer)
        cache.set(value or '', result)
        return result

class LanguageField(forms.ChoiceField):
    """
    A language field for Django forms.
    """
    widget = _LanguageWidget

    def __init__(self, *args, **kwargs):
        defaults = {'choices': _get_sorted_languages()}
        defaults.update(kwargs)
        super().__init__(*args, **defaults)
