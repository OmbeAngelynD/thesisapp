from django.contrib import admin

# Register your models here.

from thesis_app.models import Student, Thesis, Advisor

admin.site.register(Student)
admin.site.register(Thesis)
admin.site.register(Advisor)
