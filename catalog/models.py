from django.db import models
from django.core import validators
from djmoney.models.fields import MoneyField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.conf import settings
from djmoney.contrib.exchange.models import convert_money
from djmoney.money import Money
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    is_organiser = models.BooleanField(default=True) #askar and me
    is_manager = models.BooleanField(default=False) #others

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username

class Organisation(models.Model):
    name = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=100, blank=True)
    phone = PhoneNumberField(null=True , blank=True)
    email = models.EmailField(null=True)
    bank = models.CharField(max_length=50, null=True, blank=True)
    bank_acc = models.CharField(max_length=50, null=True, blank=True)
    bik = models.CharField(max_length=20,  null=True, blank=True)
    
    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

class Brand(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50, null=True, blank=True)
    contact_person = models.CharField(max_length=100, null=True, blank=True)
    phone = PhoneNumberField(null=True , blank=True)
    email = models.EmailField(null=True, blank=True)
    bank = models.CharField(max_length=50, null=True, blank=True)
    bank_acc = models.CharField(max_length=50, null=True, blank=True)
    bik = models.CharField(max_length=20,  null=True, blank=True)
    
    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=100, blank=True)
    phone = PhoneNumberField(null=True , blank=True)
    email = models.EmailField(null=True)
    bank = models.CharField(max_length=50, null=True, blank=True)
    bank = models.CharField(max_length=50, null=True, blank=True)
    bank_acc = models.CharField(max_length=50, null=True, blank=True)
    bik = models.CharField(max_length=20,  null=True, blank=True)
    
    def __str__(self):
        return self.name

class Subcategory(models.Model):
    category = models.ForeignKey('Category', related_name = 'subcategories', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} из категории {self.category}"

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Catalog(models.Model):
    id = models.AutoField(primary_key=True, editable=True)

    name = models.CharField(max_length=150)
    brand = models.ForeignKey('Brand',on_delete=models.SET_NULL, null=True)
    model = models.CharField(max_length=25, null=True)
    article = models.CharField(max_length=25, null=True,blank=True)
    category = models.ForeignKey('Category', related_name="categories", on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey('Subcategory', related_name="subcategories", on_delete=models.SET_NULL, null=True, blank=True)
    code = models.CharField(max_length=6, null=True, blank=True)
    external_code = models.CharField(max_length=50, null=True, blank=True)
    barcode = models.CharField(max_length=16, null=True, blank=True)
    zone = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank = True)
    hs_code = models.IntegerField(null=True,blank=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    customs_tax = models.FloatField(default=1, null=True)
    
    transport_coefficient = models.FloatField(default=1.1, null=True,blank=True)
    margin_coefficient = models.FloatField(default=1.3, null=True,blank=True)
    stock_qty = models.IntegerField(default=0, null=True,blank=True)
    purchase_price = MoneyField(max_digits=14, decimal_places=2, default_currency='KZT', null=True,blank=True) #EXW
    sell_price = MoneyField(max_digits=14, decimal_places=2, default_currency='KZT', null=True,blank=True)
    min_sell_price = MoneyField(max_digits=14, decimal_places=2, default_currency='KZT', null=True,blank=True)
    max_sell_price = MoneyField(max_digits=14, decimal_places=2, default_currency='KZT', null=True,blank=True)
    image = models.ImageField(upload_to = "static/images", null= True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.model}"

    def get_order(self):
        return self.orders.get_order
    
    def convert_euro(self):
        return convert_money(self.sell_price, 'EUR')
    
    def convert_dollars(self):
        return convert_money(self.sell_price, 'USD')

    def convert_ruble(self):
        return convert_money(self.sell_price, 'RUB')
    
    def get_orders_count(self):
        items = OrderedItem.objects.filter(item = self)
        expected = 0

        for i in items:
            purchase = i.order_items.all()
            if purchase.exists():
                for p in purchase:
                    expected += i.quantity
        return expected
    
    def get_purchases_count(self):
        items = PurchasedItem.objects.filter(item = self)
        expected = 0

        for i in items:
            purchase = i.purchase_items.all()
            if purchase.exists():
                for p in purchase:
                    expected += i.quantity
        return expected

class Cart(models.Model):
    manager = models.ForeignKey('UserProfile', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50, null=True)
    items = models.ManyToManyField('OrderItem', related_name='cart_items')
    date = models.DateTimeField(default=now)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.date}" 

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price()
        return total

percentage_validators=[MinValueValidator(0.0), MaxValueValidator(100)]

class OrderItem(models.Model):
    id = models.AutoField(primary_key=True, editable=True)
    
    item = models.ForeignKey('Catalog', on_delete=models.CASCADE, related_name='cart')
    quantity = models.IntegerField(default=1)
    discount = models.FloatField(default=3, null=True, blank=True, validators=percentage_validators)

    def __str__(self):
        return f"{self.quantity} of {self.item.brand} {self.item.model}"
    
    def get_total_item_price(self):
        return self.quantity * self.item_with_discount()
    
    def item_with_discount(self):
        return self.item.sell_price - (self.discount * self.item.sell_price)/100

    def get_order(self):
        return self.order_items.all().__str__
    
    
class OrderedItem(models.Model):
    id = models.AutoField(primary_key=True, editable=True)
    
    item = models.ForeignKey('Catalog', on_delete=models.CASCADE, related_name='orders')
    quantity = models.IntegerField(default=1)
    discount = models.FloatField(default=3, null=True, blank=True, validators=percentage_validators)

    def __str__(self):
        return f"{self.quantity} of {self.item.brand} {self.item.model}"
    
    def get_total_item_price(self):
        return self.quantity * self.item_with_discount()
    
    def item_with_discount(self):
        return self.item.sell_price - (self.discount * self.item.sell_price)/100

    def get_orders_count(self):
        items = OrderedItem.objects.filter(item = self.item)
        expected = 0

        for i in items:
            purchase = i.order_items.all()
            if purchase.exists():
                for p in purchase:
                    expected += i.quantity
        return expected
    
    def get_purchases_count(self):
        items = PurchasedItem.objects.filter(item = self.item)
        expected = 0

        for i in items:
            purchase = i.purchase_items.all()
            if purchase.exists():
                for p in purchase:
                    expected += i.quantity
        return expected


class Order(models.Model):
    PENDING = 'В ожидании'
    APPROVED = 'Утвержден'
    YELLOW_BOOTS = 'Желтые ботинки'

    CHOICES_STATUS = (
        (PENDING, 'В ожидании'),
        (APPROVED, 'Утвержден'),
        (YELLOW_BOOTS, 'Желтые ботинки'),
    )

    TENGE = 'тг'
    EURO = 'евро'
    DOLLAR = '$'
    
    CHOICES_CURRENCY = (
        (TENGE, 'тг'),
        (EURO, 'евро'),
        (DOLLAR, '$'),
    )

    id = models.AutoField(primary_key=True, editable=True)

    organisation = models.ForeignKey('Organisation', on_delete=models.SET_NULL, null=True, blank=True)    
    project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True)
    name = models.CharField(max_length=50)
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=25,choices=CHOICES_STATUS, default=PENDING)
    manager = models.ForeignKey('UserProfile', on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField('OrderedItem', related_name='order_items')

    # profit = models.IntegerField(default=0)

    discount = models.FloatField(null=True, blank=True, validators=percentage_validators)
    
    # comments
    files = models.FileField(upload_to ='static/files', null=True, blank=True)
    received = MoneyField(max_digits=14, decimal_places=2, default_currency='KZT', null=True)
    shipped = models.IntegerField(default=0)
    shipment_date = models.DateField(blank=True, null=True)


    def __str__(self):
        return f"id: {self.id} {self.name}"
    
    def get_item(self):
        return f"{self.items.quantity} of {self.items.item}"
    
    def get_total_item_count(self):
        total_items = 0
        for item in self.items.all():
            total_items += item.quantity
        return total_items

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price()
        return total

    def get_debt(self):
        return self.get_total()-self.received
    
    def have_to_ship(self):
        return self.get_total_item_count()-self.shipped
    
    def convert_euro(self):
        if self.get_total() == 0:
            return (convert_money(Money(0, 'KZT'), 'EUR'))
        return convert_money(self.get_total(), 'EUR')
    
    def convert_dollars(self):
        if self.get_total() == 0:
            return (convert_money(Money(0, 'KZT'), 'USD'))
        return convert_money(self.get_total(), 'USD')

    def convert_ruble(self):
        if self.get_total() == 0:
            return (convert_money(Money(0, 'KZT'), 'RUB'))
        return convert_money(self.get_total(), 'RUB')


class Purchase(models.Model):
    UNORDERED = 'не заказано'
    UNPAID = 'не оплачено'
    PREPAID = 'предоплачено'
    PAID = 'оплачено'

    CHOICES_ORDERED_STATUS = (
        (UNORDERED, 'не заказано'),
        (UNPAID, 'не оплачено'),
        (PREPAID, 'предоплачено'),
        (PAID, 'оплачено'),
    )

    id = models.AutoField(primary_key=True, editable=True)

    organisation = models.ForeignKey('Organisation', on_delete=models.SET_NULL, null=True, blank=True)    
    project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True)
    name = models.CharField(max_length=50)
    seller = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=15, choices=CHOICES_ORDERED_STATUS, blank=True)
    manager = models.ForeignKey('UserProfile', on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField('PurchasedItem', related_name='purchase_items')
    
    discount = models.FloatField(null=True, blank=True, validators=percentage_validators)
    
    files = models.FileField(upload_to ='static/files', null=True, blank=True)
    received = models.IntegerField()
    paid = MoneyField(max_digits=14, decimal_places=2, default_currency='KZT', null=True)
    pickup_date = models.DateField(blank=True, null=True)
    
    proforma = models.CharField(max_length=15, blank=True)
    
    def __str__(self):
        return f"{self.name}"
    
    def get_item(self):
        return f"{self.items.quantity} of {self.items.item}"
    
    def get_total_item_count(self):
        total_items = 0
        for item in self.items.all():
            total_items += item.quantity
        return total_items

    def get_total(self):
        total = 0
        for p_item in self.items.all():
            total += p_item.get_total_item_price()
        return total
    
    def get_debt(self):
        return self.get_total()-self.paid
    
    def have_to_ship(self):
        return self.get_total_item_count()-self.received
    
    def convert_euro(self):
        if self.get_total() == 0:
            return (convert_money(Money(0, 'KZT'), 'EUR'))
        return convert_money(self.get_total(), 'EUR')
    
    def convert_dollars(self):
        if self.get_total() == 0:
            return (convert_money(Money(0, 'KZT'), 'USD'))
        return convert_money(self.get_total(), 'USD')

    def convert_ruble(self):
        if self.get_total() == 0:
            return (convert_money(Money(0, 'KZT'), 'RUB'))
        return convert_money(self.get_total(), 'RUB')


class PurchasedItem(models.Model):
    id = models.AutoField(primary_key=True, editable=True)
    
    item = models.ForeignKey('Catalog', on_delete=models.CASCADE, related_name='purchases')
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.brand} {self.item.model}"
    
    def get_total_item_price(self):
        return self.quantity * self.item.purchase_price
    
    def get_orders_count(self):
        items = OrderedItem.objects.filter(item = self.item)
        expected = 0

        for i in items:
            purchase = i.order_items.all()
            if purchase.exists():
                for p in purchase:
                    expected += i.quantity
        return expected
    
    def get_purchases_count(self):
        items = PurchasedItem.objects.filter(item = self.item)
        expected = 0

        for i in items:
            purchase = i.purchase_items.all()
            if purchase.exists():
                for p in purchase:
                    expected += i.quantity
        return expected

def post_user_created_signal(sender, instance, created, **kwargs):
    print(instance, created)
    if created:
        UserProfile.objects.create(user=instance)
     
post_save.connect(post_user_created_signal, sender=User)
