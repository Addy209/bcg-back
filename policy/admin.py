from django.contrib import admin
from .models import Customer,Policy_feature,Policy_tbl
# Register your models here.
admin.site.register(Customer)
admin.site.register(Policy_tbl)
admin.site.register(Policy_feature)