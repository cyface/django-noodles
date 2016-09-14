"""
Views for test cases
"""
from django.shortcuts import render


def home(request):
    return render(request, "noodles_tests/render_contact_form.html")
