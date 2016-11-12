# django-language-field
Language Field for Django apps


## Installation

`pip install django-language-field`

Add `languages` to your installed apps.

In your `models.py` file import the field `from languages.fields import LanguageField`

Use in your models:

```
class MyModel(models.Model):
    ...
    language = LanguageField()
```

If you don't want it to be required it is recommended to add `blank=True` but *not* `null=True` as it is based off of Django's `CharField`
