from django.urls import path
from .views import PerformanceView
from catalog.views import TempPageView

app_name='projects'

urlpatterns = [
#     path('', PerformanceView, name='performance'),
    path('', TempPageView.as_view(), name='performance'),
]
