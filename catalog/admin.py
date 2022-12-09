from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(REGION)
admin.site.register(NATION)
admin.site.register(CUSTOMER)
admin.site.register(PART)
admin.site.register(SUPPLIER)
admin.site.register(PARTSUPP)
admin.site.register(ORDERS)
admin.site.register(LINEITEM)