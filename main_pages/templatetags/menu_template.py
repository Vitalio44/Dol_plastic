from django import template
from main_pages.models import Page

register = template.Library()


@register.inclusion_tag('top_menu.html')
def get_page_list(active_page=None):
    return {'top_menus': Page.objects.order_by('menu_position'), 'act_page': active_page}