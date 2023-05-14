from django.contrib import admin

# Register your models here.
from .models import *

from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Categories)
admin.site.register(Color)
admin.site.register(DriverType)
admin.site.register(AudioSpecification)
admin.site.register(Battery)
admin.site.register(Physical)
admin.site.register(Connectivity)
admin.site.register(Controls)
admin.site.register(Characteristics)
admin.site.register(Types)
admin.site.register(ProductImage)

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
