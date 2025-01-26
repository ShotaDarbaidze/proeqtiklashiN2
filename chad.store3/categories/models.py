from django.db import models
from config.util_models.models import TimeStampModel

class Category(TimeStampModel):
    name = models.CharField(max_length = 255 , unique = True)
    products = models.ManyToManyField('products.Product' , related_name = 'categories')
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'CAtegories'
    
    
class CategoryImage(TimeStampModel):
    category = models.ForeignKey('categories.Category',related_name = 'image',on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'categories/')
    
