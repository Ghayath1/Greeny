from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify

# Create your models here.

FLAG_TYPE = (
    ('New', 'New'),
    ('Feature' , 'Feature'),
    ('Sale' , 'Sale')
)


class Product(models.Model):
    name = models.CharField(_('Name'),max_length=150)
    subtitle = models.CharField(_('Subtitle'),max_length=300)
    description = models.TextField(_('Description'),max_length=10000)
    sku = models.IntegerField()
    price = models.FloatField()
    video_url = models.URLField(_('Video URL'),null=True,blank=True)
    category = models.ForeignKey('Category' ,verbose_name=_('Category'),related_name='product_category',on_delete=models.CASCADE)
    brand = models.ForeignKey('Brand' ,verbose_name=_('Brand'), related_name='product_brand',on_delete=models.CASCADE)
    image = models.ImageField(_('Image'),upload_to=('products/'))
    flag = models.CharField(_('Flag'),choices=FLAG_TYPE, max_length=10)
    tags = TaggableManager()
    slug = models.SlugField(null=True,blank=True)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
       self.slug = slugify(self.name)    
       super(Product, self).save(*args, **kwargs) # Call the real save() method
   
class ProductImage(models.Model):
    product = models.ForeignKey(Product ,verbose_name=_('Product'), on_delete=models.CASCADE , related_name='product_image')
    image = models.ImageField(_('Image'),upload_to = 'product_images')

    def __str__(self):
        return str(self.product)

class Category(models.Model):
    name = models.CharField(_('Name') , max_length=100)  
    image = models.ImageField(_('Image'),upload_to='category/') 
    slug = models.SlugField(null=True,blank=True)

      
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
       self.slug = slugify(self.name)    
       super(Category, self).save(*args, **kwargs)

class Brand(models.Model):
    name = models.CharField(_('Name'),max_length=100)
    image = models.ImageField(_('Image'),upload_to='brand/')
    category = models.ForeignKey(Category,verbose_name=_('Category'), related_name='brand_category',on_delete=models.CASCADE)
    slug = models.SlugField(null=True,blank=True)

     
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
       self.slug = slugify(self.name)    
       super(Brand, self).save(*args, **kwargs)

class ProductReview(models.Model):
    user = models.ForeignKey(User,verbose_name=_('User'),on_delete=models.SET_NULL, null=True,blank=True)
    product = models.ForeignKey(Product,verbose_name=_('Product'),related_name='product_review',on_delete=models.CASCADE)
    review = models.CharField(_('Review'),max_length=400)
    rate = models.IntegerField(_('Rate'))
    created_at = models.DateTimeField(_('Created at'), default=timezone.now)

    def __str__(self):
        return str(self.user)
    
 