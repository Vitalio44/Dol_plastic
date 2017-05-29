from django.shortcuts import render
from main_pages.models import Page

def show_page(request, page_slug):
    context_dict = {}
    try:
        page = Page.objects.get(slug=page_slug)
        context_dict['page'] = page
    except Page.DoesNotExist:
        context_dict['page'] = None
    return render(request, 'page.html', context_dict)
