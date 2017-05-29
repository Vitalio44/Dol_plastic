from django import template
from main_pages.models import MainMenu

register = template.Library()


@register.inclusion_tag('main_menu.html')
def get_main_menu(active_page=None):
    return {'m_menus': MainMenu.objects.order_by('menu_position'), 'act_menu': active_page}