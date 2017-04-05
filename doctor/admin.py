from django.contrib import admin
from .models import Doctor


class DoctorAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp"]
    list_display_links = ["title"]
    list_filter = ["timestamp"]
    search_fields = ["title"]
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = Doctor



admin.site.register(Doctor, DoctorAdmin)
