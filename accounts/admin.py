from django.contrib import admin
from .models import Section , SectionUser , Workers

admin.site.register(SectionUser)
admin.site.register(Section)
admin.site.register(Workers)