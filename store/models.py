from django.db import models

# Create your models here.
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


class Physical(models.Model):
    collapsible = models.BooleanField(default=True)
    water_resistance = models.BooleanField(default=False)
    charging_time = models.DecimalField(max_digits=2, decimal_places=1)
    color = models.ForeignKey('Color', on_delete=models.CASCADE)
    weight = models.IntegerField()

    def __str__(self):
        return f'collapsible: {self.collapsible}\nwater_resistance: {self.water_resistance}\ncharging_time: {self.charging_time}\ncolor: {self.color.name}\nweight: {self.weight}\n'


class Connectivity(models.Model):
    name = models.CharField(max_length=100, default='Wire')

    def __str__(self):
        return f'{self.name}'
