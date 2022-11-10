from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from catalog.views import landing_page, LandingPageView, SignupView, TempPageView 

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',LandingPageView.as_view(), name="landing-page"),    
    path('catalog/', include('catalog.urls', namespace="catalog")),
    path('orders/', include('orders.urls', namespace="orders")),
    path('purchases/', include('purchases.urls', namespace="purchases")),

    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('temp/', TempPageView.as_view(), name='temp'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
