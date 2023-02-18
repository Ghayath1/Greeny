from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Product,ProductImage,ProductReview,Category,Brand
from django.db.models.aggregates import Avg
# Register your models here.

class ProductImageAdmin(admin.TabularInline):
    model = ProductImage

class ProductAdmin(SummernoteModelAdmin):
    list_display = ['name','flag','category','brand','price']
    inlines = [ProductImageAdmin]
    prepopulated_fields = {"slug": ("name",)}
    summernote_fields = '__all__'
    search_fields = ['name','description','subtitle']
    list_filter = ['flag','brand','category']



    def review_count(self, obj):
        return obj.product_review.count()

    def rate_avg(self,obj):
        avg = obj.product_review.aggregate(Avg('rate'))
        if avg['rate__avg']:
            return avg['rate__avg']
        return 0

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user','product','rate','review',]

   


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','category_count']

    def category_count(self, obj):
        return obj.product_category.count()


class BrandAdmin(admin.ModelAdmin):
    list_display = ['name','product_count']
    
    def product_count(self, obj):
        return obj.product_brand.count()

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductReview,ReviewAdmin)
admin.site.register(ProductImage)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Brand,BrandAdmin)