from django.contrib import admin
from .models import Product

admin.site.site_header = 'Phenomenal Shop'
admin.site.index_title = 'Main Admin'
admin.site.site_title = 'Phenomenal Shop Backend'


class ProductsAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'price','detail', 'size', 'quantity', 'imagePath']
	list_editable = ['name', 'price', 'detail','size', 'quantity', 'imagePath']


admin.site.register(Product, ProductsAdmin)
