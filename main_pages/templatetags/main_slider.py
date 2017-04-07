from django import template
from main_pages.models import Slide

register = template.Library()


@register.inclusion_tag('main_slider.html')
def get_slide_list(active_slide=None):
    return {'main_slider': Slide.objects.order_by('slide_position'), 'act_slide': active_slide}