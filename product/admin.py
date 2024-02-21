from django.contrib import admin
from product.models import Product,ProductDetail,ProductImage,Category,TableRow


class ProductsDetailInline(admin.StackedInline):
    model = ProductDetail
    extra = 1

class TableRowInline(admin.StackedInline):
    model = TableRow
    extra = 1


class ProductImageInLine(admin.StackedInline):
    model = ProductImage
    readonly_fields = ['name']
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductsDetailInline,ProductImageInLine,TableRowInline]
    list_display = ['admin_thumbnail','available']
    list_filter = ['available','categories']


    
admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
