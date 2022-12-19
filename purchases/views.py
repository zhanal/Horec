from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from catalog.models import Purchase, Cart, OrderedItem, PurchasedItem
from catalog.filters import PurchaseFilter
from requests import request
from .forms import PurchaseModelForm
from django.http import FileResponse, HttpResponse
import io
from django.template.loader import get_template
from xhtml2pdf import pisa

# class purchase_invoice(LoginRequiredMixin, generic.DetailView):
#     def get(self, *args, **kwargs):
#         try:
#             purchase = self.get_object()
#             context ={
#                 'purchase': purchase
#             }
#             return render(self.request, "purchases/purchase_invoice.html", context)
#         except ObjectDoesNotExist:
#             messages.warning(self.request, "Заказ не найден")
#             return redirect("purchases/purchase_detail.html", context)

#     def get_queryset(self):
#         return Purchase.objects.all()

# def render_to_pdf(template_src, context_dict={}):
#     template = get_template(template_src)
#     html  = template.render(context_dict)
#     result = io.BytesIO()
#     pdf = pisa.pisaDocument(io.BytesIO(html.encode('UTF-8')), result, encoding='utf-8')
#     # pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), result)
    
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='application/pdf')
#     return None

# class GenerateInvoicePdf(LoginRequiredMixin, generic.DetailView):
#     def get(self, request, *args, **kwargs):
#         try:
#             purchase = self.get_object()
#             context ={
#                 'purchase': purchase
#             }
#             pdf = render_to_pdf('purchase/purchase_invoice.html', context)
#             # pdf = pisa.CreatePDF('orders/order_invoice.html', context, encoding='UTF-8')
#             return HttpResponse(pdf, content_type='application/pdf')
#         except ObjectDoesNotExist:
#             messages.warning(self.request, "Заказ не найден")
#             return redirect("purchases/purchase_detail.html", context)
    
#     def get_queryset(self):
#         return Purchase.objects.all()

@login_required
def PurchaseListView(request):
    purchases = Purchase.objects.all()
    filter = PurchaseFilter(request.GET, queryset=purchases)
    purchases = filter.qs
    context = {
        "purchases": purchases,
        "filter": filter,
    }
    return render(request, "purchases/purchase_list.html", context)

# class PurchaseListView(LoginRequiredMixin, generic.ListView):
#     template_name = "purchases/purchase_list.html"

#     def get_queryset(self):
#         return Purchase.objects.all()

class PurchaseCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "purchases/purchase_create.html"
    form_class= PurchaseModelForm

    def get_success_url(self):
        return reverse("purchases:purchase-list")
    
    def form_valid(self, form):
        purchase = form.save(commit=False) #doesn't save to a db but a python object
        purchase.manager = self.request.user.userprofile
        purchase.save() #now commits to a db
        return super(PurchaseCreateView, self).form_valid(form)
    
class PurchaseDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "purchases/purchase_detail.html"

    def get(self, *args, **kwargs):
        try:
            purchase = self.get_object()
            context ={
                'purchase': purchase
            }
            return render(self.request, "purchases/purchase_detail.html", context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "Закупка не найдена")
            return redirect("/purchases")

    def get_queryset(self):
        return Purchase.objects.all()

class PurchaseUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "purchases/purchase_update.html"
    form_class = PurchaseModelForm

    def get_success_url(self):
        return reverse("purchases:purchase-list")

    def get_queryset(self):
        return Purchase.objects.all()

class PurchaseDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "purchases/purchase_delete.html"
    context_object_name = "purchase"

    def get_success_url(self):
        return reverse("purchases:purchase-list")

    def get_queryset(self):
        return Purchase.objects.all()


@login_required
def add_to_purchase(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)
    cart_qs = Cart.objects.filter(
        manager= request.user.userprofile,
        ordered=False)
    purchase_items = purchase.items.all()

    # if cart.exists():
    if cart_qs.exists():
        cart = cart_qs[0] #the only avaliable cart
        cart_items = cart.items.all() #queryset!
        if purchase_items.exists():
            for i in cart_items:
                for j in purchase_items:
                    if i.item == j.item:
                        j.quantity += i.quantity
                        j.save()
                        cart.items.remove(i)
                        # i.quantity -= i.quantity
                        i.save()
                        messages.info(request, "Товары увеличились")
                        return redirect("purchases:purchase-detail", pk=pk)
                    else:
                        purchase.items.create(item=i.item, quantity=i.quantity)
                        cart.items.remove(i)
                        messages.info(request, "Добавлен новый товар в закупки :)")
                        return redirect("purchases:purchase-detail", pk=pk)
        else:
            for i in cart_items:
                purchase.items.create(item=i.item, quantity=i.quantity)
                cart.items.remove(i)
                messages.info(request, "Товар добавлен :)")
                return redirect("purchases:purchase-detail", pk=pk)
    else:
        messages.info(request, "Отказано, так как корзина пуста)")
    return redirect("purchases:purchase-detail", pk=pk)

@login_required
def add_single_item_to_purchase(request, pk):
    purchased_item = get_object_or_404(PurchasedItem, pk=pk)
    purchase = purchased_item.purchase_items.get()

    if purchase.items.filter(pk = purchased_item.pk).exists():
        purchased_item.quantity += 1
        purchased_item.save()
        messages.info(request, "+1")
        return redirect("purchases:purchase-detail", pk=purchase.pk)
    else:
        messages.info(request, "Этого товара даже не было в корзине")
        return redirect("purchases:purchase-detail", pk=purchase.pk)

@login_required
def remove_single_item_from_purchase(request, pk):
    purchased_item = get_object_or_404(PurchasedItem, pk=pk)
    purchase = purchased_item.purchase_items.get()

    if purchase.items.filter(pk = purchased_item.pk).exists():
        if purchased_item.quantity > 1:
            purchased_item.quantity -= 1
            purchased_item.save()
        else:
            purchase.items.remove(purchased_item)
            purchased_item.delete()

        messages.info(request, "-1")
        return redirect("purchases:purchase-detail", pk=purchase.pk)
    else:
        messages.info(request, "Этого товара даже не было в корзине")
        return redirect("purchases:purchase-detail", pk=purchase.pk)

@login_required
def open_file(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)
    file = purchase.files

    if file:
        response = FileResponse(file.open(), filename=file.name)
        return response
    else:
        messages.info(request, "Файл не найден")
        return redirect("purchases:purchase-detail", pk=pk)
