from django.db.models.fields import CharField

class LanguageField(CharField):
    """
    A language field for Django models.
    """
    def __init__(self, *args, db_collation=None, **kwargs):
        # Local import so the languages aren't loaded unless they are needed.
        from .languages import LANGUAGES

        kwargs.setdefault('max_length', 3)
        kwargs.setdefault('choices', LANGUAGES)
        super().__init__(*args, db_collation, **kwargs)
