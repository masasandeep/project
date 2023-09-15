from django.contrib import admin
from .models import *
admin.site.register(User)
admin.site.register(TestResults)
admin.site.register(Reports)
admin.site.register(Testcategories)
admin.site.register(MainDivisions)
# Register your models here.
