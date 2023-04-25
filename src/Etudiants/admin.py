from django.contrib import admin
from Etudiants.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "password", )
    list_editable = ["email", "password", ]

admin.site.register(Student, StudentAdmin)
