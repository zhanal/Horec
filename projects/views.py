from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

@login_required
def PerformanceView(request):
    return render(request, "projects\performance.html")

# class PerformanceView(LoginRequiredMixin, generic.DetailView):
    # template_name = "projects\performance.html"
