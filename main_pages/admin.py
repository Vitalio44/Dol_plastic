from django.contrib import admin
from .models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp", "menu_name", "menu_position"]
    list_display_links = ["title"]
    list_filter = ["timestamp"]
    search_fields = ["title"]
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = Page



admin.site.register(Page, PageAdmin)

