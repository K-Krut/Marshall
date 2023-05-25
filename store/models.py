import uuid
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    img = models.ImageField(upload_to=f"img/category", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class DriverType(models.Model):
    name = models.CharField(max_length=100, default="Dynamic")

    def __str__(self):
        return f'{self.name}'


class AudioSpecification(models.Model):
    driver_sensitivity = models.IntegerField()
    deriver_type = models.ForeignKey("DriverType", on_delete=models.DO_NOTHING)
    driver_impedance = models.IntegerField()
    frequency_range = models.CharField(max_length=100)
    drivers = models.IntegerField()

    def __str__(self):
        return f'driver_sensitivity: {self.driver_sensitivity}\nderiver_type: {self.deriver_type.name}\ndriver_impedance: {self.driver_impedance}\nfrequency_range:  {self.frequency_range}\ndrivers: {self.drivers} '


class Battery(models.Model):
    play_time = models.IntegerField()
    wireless_charging = models.BooleanField(default=False)
    charging_time = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return f'play_time: {self.play_time}\nwireless_charging: {self.wireless_charging}\ncharging_time: {self.charging_time}\n'


class Controls(models.Model):
    remote = models.BooleanField(default=True)
    microphone = models.BooleanField(default=True)
    noise_cancellation = models.BooleanField(default=False)
    connectivity = models.ForeignKey("Connectivity", on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'remote: {self.remote}\nmicrophone: {self.microphone}\nnoise_cancellation: {self.noise_cancellation}\nconnectivity: {self.connectivity}\n'


class Physical(models.Model):
    collapsible = models.BooleanField(default=True)
    water_resistance = models.BooleanField(default=False)
    charging_time = models.DecimalField(max_digits=2, decimal_places=1)
    color = models.ForeignKey('Color', on_delete=models.CASCADE)
    weight = models.IntegerField()

    def __str__(self):
        return f'collapsible: {self.collapsible}\nwater_resistance: {self.water_resistance}\ncharging_time: {self.charging_time}\ncolor: {self.color.name}\nweight: {self.weight}\n '


class Connectivity(models.Model):
    name = models.CharField(max_length=100, default='Wire')

    def __str__(self):
        return f'{self.name}'


class Characteristics(models.Model):
    # product = models.ForeignKey("Product", on_delete=models.CASCADE, null=True)
    audio = models.ForeignKey(AudioSpecification, on_delete=models.CASCADE, null=True)
    battery = models.ForeignKey(Battery, on_delete=models.CASCADE, null=True)
    physical = models.ForeignKey(Physical, on_delete=models.CASCADE, null=True)
    connectivity = models.ForeignKey(Connectivity, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.audio}\n{self.battery}\n{self.physical}\n{self.connectivity}'


class Types(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, db_index=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='products/')
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(Types, on_delete=models.CASCADE, null=True)
    characteristics = models.ForeignKey(Characteristics, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.id} --> {self.name}'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.FileField("img", upload_to=f"img/%Y/%m/%d/")

    def __str__(self):
        return self.product.name

class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    @property
    def total(self):
        items = self.cartitems.all()
        total = sum([item.price for item in items])
        return total

    @property
    def count(self):
        items = self.cartitems.all()
        quantity = sum([item.quantity for item in items])
        return quantity

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartitems')
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.product.name)

    @property
    def price(self):
        return self.product.price * self.quantity

# class Order(models.Model):
#
#
