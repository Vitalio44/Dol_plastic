from django.contrib import admin
from .models import Doctor, Specialization


class DoctorAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp"]
    list_display_links = ["title"]
    list_filter = ["timestamp"]
    search_fields = ["title"]
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = Doctor

class SpecializationAdmin(admin.ModelAdmin):
    list_display = ["name", "timestamp"]
    list_display_links = ["name"]
    list_filter = ["timestamp"]
    search_fields = ["name"]

    class Meta:
        model = Specialization


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Specialization, SpecializationAdmin)
