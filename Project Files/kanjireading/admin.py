from django.contrib import admin

from .models import Kanji, Reading

# Register your models here.
admin.site.register(Kanji)
admin.site.register(Reading)