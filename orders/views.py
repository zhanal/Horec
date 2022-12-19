from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from django.shortcuts import redirect, reverse, render, get_object_or_404
from requests import request
from catalog.filters import OrderFilter
from catalog.models import Order, Cart, OrderedItem
from .forms import OrderModelForm
from django.http import FileResponse, HttpResponse
import io
from django.template.loader import get_template
from xhtml2pdf import pisa

class order_invoice(LoginRequiredMixin, generic.DetailView):
    def get(self, *args, **kwargs):
        try:
            order = self.get_object()
            context ={
                'order': order
            }
            return render(self.request, "orders/order_invoice.html", context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "Заказ не найден")
            return redirect("orders/order_detail.html", context)

    def get_queryset(self):
        return Order.objects.all()


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode('UTF-8')), result, encoding='utf-8')
    # pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), result)
    
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

class GenerateInvoicePdf(LoginRequiredMixin, generic.DetailView):
    def get(self, request, *args, **kwargs):
        try:
            order = self.get_object()
            context ={
                'order': order
            }
            pdf = render_to_pdf('orders/order_invoice.html', context)
            # pdf = pisa.CreatePDF('orders/order_invoice.html', context, encoding='UTF-8')
            return HttpResponse(pdf, content_type='application/pdf')
        except ObjectDoesNotExist:
            messages.warning(self.request, "Заказ не найден")
            return redirect("orders/order_detail.html", context)
    
    def get_queryset(self):
        return Order.objects.all()

@login_required
def OrderListView(request):
    orders = Order.objects.all()
    filter = OrderFilter(request.GET, queryset=orders)
    orders = filter.qs
    context = {
        "orders": orders,
        "filter": filter,
    }
    return render(request, "orders/order_list.html", context)

# class OrderListView(LoginRequiredMixin, generic.ListView):
#     template_name ="orders/order_list.html"
    
#     def get_queryset(self):
#         return Order.objects.all()

class OrderCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "orders/order_create.html"
    form_class= OrderModelForm
    
    def get_success_url(self):
        return reverse("orders:order-list")
          
    def form_valid(self, form):
        order = form.save(commit=False) #doesn't save to a db but a python object
        order.manager = self.request.user.userprofile
        order.save() #now commits to a db
        return super(OrderCreateView, self).form_valid(form)

class OrderDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "orders/order_detail.html"

    def get(self, *args, **kwargs):
        try:
            order = self.get_object()
            context ={
                'order': order
            }
            return render(self.request, "orders/order_detail.html", context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "Заказ не найден")
            return redirect("/orders")

    def get_queryset(self):
        return Order.objects.all()

class OrderUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "orders/order_update.html"
    form_class= OrderModelForm

    def get_success_url(self):
        return reverse("orders:order-list")

    def get_queryset(self):
        return Order.objects.all()    

class OrderDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "orders/order_delete.html"
    context_object_name = "order"

    def get_success_url(self):
        return reverse("orders:order-list")

    def get_queryset(self):
        return Order.objects.all()

@login_required
def add_to_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    cart_qs = Cart.objects.filter(
        manager= request.user.userprofile,
        ordered = False)
    order_items = order.items.all()

    # if cart.exists():
    if cart_qs.exists():
        cart = cart_qs[0] #the only avaliable cart
        cart_items = cart.items.all() #queryset!
        if order_items.exists():
            for i in cart_items:
                for j in order_items:
                    if i.item == j.item:
                        j.quantity += i.quantity
                        j.save()
                        cart.items.remove(i)
                        # i.quantity -= i.quantity
                        i.save()
                        messages.info(request, "Товары увеличились")
                        return redirect("orders:order-detail", pk=pk)
                    else:
                        order.items.create(item=i.item, quantity=i.quantity)
                        cart.items.remove(i)
                        messages.info(request, "Добавлен новый товар :)")
                        return redirect("orders:order-detail", pk=pk)
        else:
            for i in cart_items:
                order.items.create(item=i.item, quantity=i.quantity)
                cart.items.remove(i)
                messages.info(request, "Товар добавлен :)")
                return redirect("orders:order-detail", pk=pk)
    else:
        messages.info(request, "Отказано, так как корзина пуста)")
    return redirect("orders:order-detail", pk=pk)

@login_required
def add_single_item_to_order(request, pk):
    ordered_item = get_object_or_404(OrderedItem, pk=pk)
    order = ordered_item.order_items.get()

    if order.items.filter(pk = ordered_item.pk).exists():
        ordered_item.quantity += 1
        ordered_item.save()
        messages.info(request, "+1")
        return redirect("orders:order-detail", pk=order.pk)
    else:
        messages.info(request, "Этого товара даже не было в корзине")
        return redirect("orders:order-detail", pk=order.pk)

@login_required
def remove_single_item_from_order(request, pk):
    ordered_item = get_object_or_404(OrderedItem, pk=pk)
    order = ordered_item.order_items.get()

    if order.items.filter(pk = ordered_item.pk).exists():
        if ordered_item.quantity > 1:
            ordered_item.quantity -= 1
            ordered_item.save()
        else:
            order.items.remove(ordered_item)
            ordered_item.delete()
            # all good
        messages.info(request, "-1")
        return redirect("orders:order-detail", pk=order.pk)
    else:
        messages.info(request, "Этого товара даже не было в корзине")
        return redirect("orders:order-detail", pk=order.pk)

@login_required
def open_file(request, pk):
    order = get_object_or_404(Order, pk=pk)
    file = order.files

    if file:
        response = FileResponse(file.open(), filename=file.name)
        return response
    else:
        messages.info(request, "Файл не найден")
        return redirect("orders:order-detail", pk=pk)
