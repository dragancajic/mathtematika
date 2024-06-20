from django.contrib import admin

# укључи моделе / класе за моделовање стварних објеката (ентитета)
from .models import Location, Preference, User

# Register your models here.
# након укључења/import-овања модел класа, региструј их овдје
admin.site.register(Location)
admin.site.register(Preference)
admin.site.register(User)
