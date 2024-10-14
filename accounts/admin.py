from django.contrib import admin
from .models import Section , SectionUser , Workers , Help

admin.site.register(SectionUser)
admin.site.register(Section)
admin.site.register(Workers)
admin.site.register(Help)