from django.db import models
from core.models import Language
from django_cleanup import cleanup



@cleanup.select
class Category(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL,related_name='subs')

class Product(models.Model):
    code = models.PositiveBigIntegerField()
    thumbnail = models.ImageField()
    available = models.BooleanField(default=True)
    recommended = models.BooleanField(default=False)
    sold = models.PositiveBigIntegerField(default=0)
    view = models.PositiveBigIntegerField(default=0)
    categories = models.ManyToManyField(Category,related_name='products')

    @property
    def admin_thumbnail(self):
       return mark_safe('<img style="height:125px;" src="%s" />' % self.thumbnail.url)

class ProductDetail(models.Model):
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    language = models.ForeignKey(Language,on_delete = models.PROTECT)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()
    date = models.DateField(auto_now=True)


@cleanup.select
class ProductImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='images')

    def save(self, *args, **kwargs):
        self.name = f"{self.product.name}-{self.id}" 
        super(ProductImage,self).save(*args, **kwargs)


class TableRow(models.Model):
    language = models.ForeignKey(Language,on_delete = models.PROTECT)
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='tablerows')

    def __str__(self):
        return f"{self.product.name}-{self.id}"


