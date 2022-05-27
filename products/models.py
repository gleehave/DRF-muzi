from django.db import models

from core.timestamp import TimeStampedModel


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name

class Type(models.Model):
    name                = models.CharField(max_length=100)
    thumbnail_image_url = models.URLField(max_length=2000)
    category            = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='type')

    class Meta:
        db_table = 'types'

class Product(TimeStampedModel):
    name                  = models.CharField(max_length=500)
    price                 = models.DecimalField(max_digits=9, decimal_places=2)
    description           = models.TextField()
    thumbnail_image_url   = models.URLField(max_length=2000)

    type                  = models.ForeignKey('Type', on_delete=models.CASCADE, related_name='product')
    tags                  = models.ManyToManyField('Tag', through='TagProduct', related_name='products')

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name

class Tag(models.Model):
    name     = models.CharField(max_length=100)

    class Meta:
        db_table = 'tags'

    def __str__(self):
        return self.name

class TagProduct(models.Model):
    tag     = models.ForeignKey('Tag', on_delete=models.CASCADE, related_name='middle_product')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='middle_tag')

    class Meta:
        db_table = 'tags_products'

class ProductOption(models.Model):
    product  = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='option')
    size     = models.ForeignKey('Size', on_delete=models.CASCADE, related_name='product')
    color    = models.ForeignKey('Color', on_delete=models.CASCADE, related_name='product')
    stock    = models.IntegerField(default=1)

    class Meta:
        db_table = 'products_options'

class Image(TimeStampedModel):
    image_url = models.URLField(max_length=2000)
    product   = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='image')

    class Meta:
        db_table = 'images'

class Size(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'sizes'

class Color(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'colors'

class Promote(models.Model):
    name      = models.CharField(max_length=100)
    image_url = models.URLField(max_length=2000)

    class Meta:
        db_table = 'promotes'

class Landing(models.Model):
    image_url = models.URLField(max_length=2000)

    class Meta:
        db_table = 'landing_images'