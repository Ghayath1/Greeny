from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Product,ProductImage,ProductReview,Category,Brand
# Register your models here.

class ProductImageAdmin(admin.TabularInline):
    model = ProductImage

class ProductAdmin(SummernoteModelAdmin):
    list_display = ['name','flag','price']
    inlines = [ProductImageAdmin]
    prepopulated_fields = {"slug": ("name",)}
    summernote_fields = '__all__'


admin.site.register(Product,ProductAdmin)
admin.site.register(ProductReview)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Brand)