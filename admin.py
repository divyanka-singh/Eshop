from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(signup)
admin.site.register(category)
admin.site.register(product)
admin.site.register(order_dtls)
