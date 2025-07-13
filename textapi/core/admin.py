from django.contrib import admin
from .models import Paragraph, WordIndex

# Register the Paragraph model, WordIndex model so it appears in the Django Admin UI

admin.site.register(Paragraph)
admin.site.register(WordIndex)

