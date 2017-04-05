from django.shortcuts import render, get_object_or_404
from .models import Doctor


def doctor_detail(request, slug=None):
    doctors = get_object_or_404(Doctor, slug=slug)
    context = {
        "doctors": doctors,
        "title": doctors.title,
    }
    return render(request, "doctor.html", context)