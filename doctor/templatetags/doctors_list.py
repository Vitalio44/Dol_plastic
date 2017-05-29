from django import template
from doctor.models import Doctor, Specialization

register = template.Library()


@register.inclusion_tag('doctors_list.html')
def get_doctors_list(request):
    special_list = Specialization.objects.all()
    return {
        'doctors_list': Doctor.objects.prefetch_related('special'),
        'spec_list': special_list
    }