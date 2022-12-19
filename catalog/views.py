from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from django.views import generic
from numpy import product 
from requests import request
from .models import Catalog, Category, OrderItem, Order, Cart, Brand, Client, Organisation, Manager, User 
from .forms import CatalogModelForm, CustomUserCreationForm, DetailedCatalogModelForm, BrandModelForm, ClientModelForm, OrganisationModelForm
from .filters import CatalogFilter

#CRUD+L = create, retrieve, update and delete + list

def page_not_found(request, exception):
    return render(request, '404.html', status=404)

@login_required
def DatabaseView(request):
    context = {
        "brands_count": Brand.objects.all().count(),
        "clients_count": Client.objects.all().count(),
        "organisations_count": Organisation.objects.all().count(),
        "managers_count": User.objects.all().count(),
    }
    return render(request, "database/database.html", context)

@login_required
def BrandsListView(request):
    brands = Brand.objects.all()
    # filter = CatalogFilter(request.GET, queryset=catalog)
    # catalog = filter.qs
    context = {
        "brands": brands,
        # "filter": filter,
    }
    return render(request, "database/brands.html", context)

class BrandCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "database/brand_create.html"
    form_class = BrandModelForm
    
    def get_success_url(self):
        return reverse("brands")

class BrandUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "database/brand_update.html"
    form_class = BrandModelForm
    queryset = Brand.objects.all()
    context_object_name = 'brand'

    def get_success_url(self):
        return reverse("brands") 

class BrandDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "database/brand_delete.html"
    queryset = Brand.objects.all()
    context_object_name = 'brand'
    
    def get_success_url(self):
        return reverse("brands") 

@login_required
def ClientsListView(request):
    clients = Client.objects.all()
    # filter = CatalogFilter(request.GET, queryset=catalog)
    # catalog = filter.qs
    context = {
        "clients": clients,
        # "filter": filter,
    }
    return render(request, "database/clients.html", context)

class ClientCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "database/client_create.html"
    form_class = ClientModelForm
    
    def get_success_url(self):
        return reverse("clients")

class ClientUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "database/client_update.html"
    form_class = ClientModelForm
    queryset = Client.objects.all()
    context_object_name = 'client'

    def get_success_url(self):
        return reverse("clients") 

class ClientDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "database/client_delete.html"
    queryset = Client.objects.all()
    context_object_name = 'client'
    
    def get_success_url(self):
        return reverse("clients") 


@login_required
def OrganisationsListView(request):
    organisations = Organisation.objects.all()
    # filter = CatalogFilter(request.GET, queryset=catalog)
    # catalog = filter.qs
    context = {
        "organisations": organisations,
        # "filter": filter,
    }
    return render(request, "database/organisations.html", context)

class OrganisationCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "database/organisation_create.html"
    form_class = OrganisationModelForm
    
    def get_success_url(self):
        return reverse("organisations")

class OrganisationUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "database/organisation_update.html"
    form_class = OrganisationModelForm
    queryset = Organisation.objects.all()
    context_object_name = 'organisation'

    def get_success_url(self):
        return reverse("organisations") 

class OrganisationDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "database/organisation_delete.html"
    queryset = Organisation.objects.all()
    context_object_name = 'organisation'
    
    def get_success_url(self):
        return reverse("organisations") 


@login_required
def ManagersListView(request):
    managers = User.objects.all()
    # filter = CatalogFilter(request.GET, queryset=catalog)
    # catalog = filter.qs
    context = {
        "managers": managers,
        # "filter": filter,
    }
    return render(request, "database/managers.html", context)

class TempPageView(generic.TemplateView, LoginRequiredMixin):
    template_name = "temp.html"

class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


@login_required
def CatalogListView(request):
    catalog = Catalog.objects.all()
    filter = CatalogFilter(request.GET, queryset=catalog)
    catalog = filter.qs
    context = {
        "catalog": catalog,
        "filter": filter,
    }
    return render(request, "catalog/catalog_list.html", context)


@login_required
def CatalogLineListView(request):
    catalog = Catalog.objects.all()
    filter = CatalogFilter(request.GET, queryset=catalog)
    catalog = filter.qs
    context = {
        "catalog": catalog,
        "filter": filter,
    }
    return render(request, "catalog/catalog_line_list.html", context)

# class CatalogListView(LoginRequiredMixin, generic.ListView):
#     template_name = "catalog/catalog_list.html"
#     queryset = Catalog.objects.all()
#     context_object_name = 'products'
#     #queryset we want to list in this template. it'll be passed into the context. Don't forget to pass this in APP's urls
#     #CatalogListView doesn't need context, ListView automatically assigns "object_list": products

class CatalogDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "catalog/catalog_detail.html"
    context_object_name = 'product'  #it'll automatically grab the product pk

    def get_queryset(self):
        return Catalog.objects.all()

def catalog_detail(request, pk):
    product = Catalog.objects.get(id=pk)
    context = {
        "product": product,
    }

    return render(request, "catalog/catalog_detail.html", context)

class CatalogCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "catalog/catalog_create.html"
    form_class = CatalogModelForm
    
    def get_success_url(self):
        return reverse("catalog:catalog-list")

def catalog_create(request):
    if request.method == 'POST':
        form = CatalogModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/catalog')

    context = {
        "form": form
    }
    return render(request, "catalog/catalog_create.html", context)


class CatalogUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "catalog/catalog_update.html"
    form_class = CatalogModelForm
    queryset = Catalog.objects.all()
    context_object_name = 'product'

    def get_success_url(self):
        return reverse("catalog:catalog-list") 

class CatalogDetailUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "catalog/catalog_detail_update.html"
    form_class = DetailedCatalogModelForm
    queryset = Catalog.objects.all()
    context_object_name = 'product'

    def get_success_url(self):
        return reverse("catalog:catalog-list") 

def catalog_update(request, pk):
    product = Catalog.objects.get(id=pk)
    form = CatalogModelForm(instance=product)
    if request.method == 'POST':
        form = CatalogModelForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/catalog')
    context = {
        "form": form,
        "product": product
    }
    return render(request, "catalog/catalog_update.html", context)


class CatalogDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "catalog/catalog_delete.html"
    queryset = Catalog.objects.all()
    context_object_name = 'product'
    
    def get_success_url(self):
        return reverse("catalog:catalog-list") 

def catalog_delete(request, pk):
    product = Catalog.objects.get(id=pk)
    product.delete()
    return redirect('/catalog')

class CategoryListView(LoginRequiredMixin, generic.ListView):
    template_name = "catalog/category_list.html"
    context_object_name = "category_list"
    queryset = Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        
        context.update({
            "unassigned_product_count": Catalog.objects.filter(category__isnull=True).count(),
            # "products_count":self.get_object().categories.all().count()
        })
        return context

class CategoryDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "catalog/category_detail.html"
    context_object_name = 'category'  #it'll automatically grab the product pk


    def get_queryset(self):
        queryset = Category.objects.all()

        return queryset

class CatalogDetailOrderView(LoginRequiredMixin, generic.DetailView):
    template_name = "catalog/catalog_orders.html"

    def get(self, *args, **kwargs):
        try:
            product = self.get_object()
            context ={
                'product': product,
            }
            return render(self.request, "catalog/catalog_orders.html", context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "Товар не найден")
            return redirect("/catalog")

    def get_queryset(self):
        return Catalog.objects.all()

class CatalogDetailPurchaseView(LoginRequiredMixin, generic.DetailView):
    template_name = "catalog/catalog_purchases.html"

    def get(self, *args, **kwargs):
        try:
            product = self.get_object()
            context ={
                'product': product,
            }
            return render(self.request, "catalog/catalog_purchases.html", context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "Товар не найден")
            return redirect("/catalog")

    def get_queryset(self):
        return Catalog.objects.all()

@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(Catalog, pk=pk)
    order_item = OrderItem.objects.get_or_create(
        item = item,
    )
    cart_qs = Cart.objects.get_or_create(  #maybe get()?
        manager= request.user.userprofile,
        ordered = False
    )
    if cart_qs[0]:
        cart = cart_qs[0]
        # check if the order item is in the order
        if cart.items.filter(item__pk = item.id).exists():
            order_item[0].quantity += 1
            order_item[0].save()
            messages.info(request, "Кол-во товара увеличилось")
            return redirect("catalog:summary") #not sure about sintax of the page
        else:
            cart.items.add(order_item[0])
            messages.info(request, "Товар добавлен в корзину")
            return redirect("catalog:catalog-list")
    else:
        cart = Cart.objects.create(name="Корзина")
        cart.items.add(order_item[0])
        messages.info(request, "Товар добавлен в корзину :)")
        return redirect("catalog:catalog-list")

@login_required
def remove_from_cart(request, pk):
    item = get_object_or_404(Catalog, pk=pk)
    cart_qs = Cart.objects.get_or_create(
        manager= request.user.userprofile,
        ordered = False,
    )
    if cart_qs[0]:
        cart = cart_qs[0]
        if cart.items.filter(item__pk = item.id).exists():
            order_item = OrderItem.objects.filter(
                item = item,
                # user=request.user,
            )[0]
            cart.items.remove(order_item)
            order_item.delete()
            messages.info(request, "Товар убран из корзины")
            return redirect("catalog:summary")
        else:
            messages.info(request, "Этого товара нет в корзине")
            return redirect("catalog:summary")
    else:
        messages.info(request, "Корзина итак пуста лол ")
        return redirect("catalog:catalog-list")

# manager=self.request.user.userprofile

@login_required
def remove_single_item_from_cart(request, pk):
    item = get_object_or_404(Catalog, pk=pk)
    cart_qs = Cart.objects.get_or_create(
        manager= request.user.userprofile,
        ordered=False
    )
    if cart_qs[0]:
        cart = cart_qs[0]
        if cart.items.filter(item__pk = item.pk).exists():
            order_item = OrderItem.objects.filter(
                item = item,
                # user = request.user,
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order_item.delete()
            messages.info(request, "-1")
            return redirect("catalog:summary")
        else:
            messages.info(request, "Этого товара даже не было в корзине")
            return redirect("catalog:catalog-detail" , pk = pk)
    else:
        messages.info(request, "В корзине нет товаров")
        return redirect("catalog:catalog-detail", pk=pk)
 
# manager=self.request.user.userprofile

class SummaryView(LoginRequiredMixin, generic.DetailView):
    template_name = "catalog/summary.html"

    def get(self, *args, **kwargs):
        try:
            cart = Cart.objects.get(
                manager= self.request.user.userprofile,
                ordered = False
            )
            context ={
                'object': cart
            }
            return render(self.request, "catalog/summary.html", context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "Корзина не найдена")
            return redirect("/catalog")

    def get_queryset(self):
        return Cart.objects.all()

