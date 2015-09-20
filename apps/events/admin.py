from django.contrib import admin
from .models import Event, Category, Comments, Assistent

admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Comments)
admin.site.register(Assistent)