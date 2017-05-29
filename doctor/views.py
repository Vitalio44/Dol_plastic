from django.shortcuts import render, get_object_or_404
from .models import Doctor, Specialization


def doctor_detail(request, slug=None):
    doctors = get_object_or_404(Doctor, slug=slug)
    context = {"doctors": doctors}
    return render(request, "doctor.html", context)


def show_spec(request):
    special_list = Specialization.objects.all()
    doctors_list = Doctor.objects.filter(special=special_list)
    context_dict = {'special_list': special_list, 'doctors_list': doctors_list}
    return render(request, "index.html", context_dict)
