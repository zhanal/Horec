from django.urls import path
from .views import PerformanceView

app_name='projects'

urlpatterns = [
    path('', PerformanceView, name='performance'),
]