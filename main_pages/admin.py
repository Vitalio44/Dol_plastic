from django.contrib import admin
from main_pages.models import Page, Slide


class PageAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp", "menu_name", "menu_position"]
    list_display_links = ["title"]
    list_filter = ["timestamp"]
    search_fields = ["title"]
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = Page


class SlideAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp", "slide_position"]
    list_display_links = ["title"]
    list_filter = ["timestamp"]
    search_fields = ["title"]

    class Meta:
        model = Slide



admin.site.register(Page, PageAdmin)
admin.site.register(Slide, SlideAdmin)

