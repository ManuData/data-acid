from django.contrib import admin

# Register all the models
from .models import Articles

# Register your models here.

admin.site.register(Articles)

