from django.contrib import admin
from .models import Product,ProductImage,ProductReview,Category,Brand
# Register your models here.

class ProductImageAdmin(admin.TabularInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','flag','price']
    inlines = [ProductImageAdmin]
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Product,ProductAdmin)
admin.site.register(ProductReview)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Brand)