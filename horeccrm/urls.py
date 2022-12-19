from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from catalog.views import(
    SignupView, TempPageView, DatabaseView, BrandsListView, ClientsListView, OrganisationsListView, ManagersListView, 
    BrandCreateView, BrandUpdateView, BrandDeleteView,
    ClientCreateView, ClientUpdateView, ClientDeleteView,
    OrganisationCreateView, OrganisationUpdateView, OrganisationDeleteView,
    )
from projects.views import PerformanceView

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', PerformanceView, name='performance'),    
    
    path('catalog/', include('catalog.urls', namespace="catalog")),
    path('orders/', include('orders.urls', namespace="orders")),
    path('purchases/', include('purchases.urls', namespace="purchases")),

    path('database/', DatabaseView, name='database'),
    path('database/brands/', BrandsListView, name='brands'),
    path('database/brands/create', BrandCreateView.as_view(), name='brands-create'),
    path('database/brands/<int:pk>/update', BrandUpdateView.as_view(), name='brands-update'),
    path('database/brands/<int:pk>/delete', BrandDeleteView.as_view(), name='brands-delete'),

    path('database/clients/', ClientsListView, name='clients'),
    path('database/clients/create', ClientCreateView.as_view(), name='clients-create'),
    path('database/clients/<int:pk>/update', ClientUpdateView.as_view(), name='clients-update'),
    path('database/clients/<int:pk>/delete', ClientDeleteView.as_view(), name='clients-delete'),

    path('database/organisations/', OrganisationsListView, name='organisations'),
    path('database/organisations/create', OrganisationCreateView.as_view(), name='organisations-create'),
    path('database/organisations/<int:pk>/update', OrganisationUpdateView.as_view(), name='organisations-update'),
    path('database/organisations/<int:pk>/delete', OrganisationDeleteView.as_view(), name='organisations-delete'),

    path('database/managers/', ManagersListView, name='managers'),

    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('temp/', TempPageView.as_view(), name='temp'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'catalog.views.page_not_found'