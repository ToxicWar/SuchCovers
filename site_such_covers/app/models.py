# coding: utf-8
from django.db import models
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager

User = get_user_model()


def upload_to(self, filename):
    return 'covers/{}'.format(filename)


class Cover(models.Model):
    title = models.CharField('Title', max_length=255)
    image = models.ImageField('Image', upload_to=upload_to)
    tags = TaggableManager()
    likes = models.IntegerField('Likes', default=0)
    is_display = models.BooleanField('Is display', default=True)

    class Meta:
        verbose_name = 'Cover'
        verbose_name_plural = 'Covers'

    def __unicode__(self):
        return self.title


class Notebook(models.Model):
    cover = models.ForeignKey(Cover, verbose_name='Cover')
    pages = models.IntegerField('Pages')

    class Meta:
        verbose_name = 'Notebook'
        verbose_name_plural = 'Notebooks'

    def __unicode__(self):
        return '{} - {}'.format(self.cover.title, self.pages)


class Order(models.Model):
    fio = models.CharField('FIO', max_length=255)
    email = models.EmailField('Email', max_length=100)
    country = models.CharField('Country', max_length=100)
    city = models.CharField('City', max_length=100)
    address = models.CharField('Address', max_length=1000)
    user = models.ForeignKey(User, verbose_name='User', null=True, blank=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __unicode__(self):
        return '{}, {}, {}'.format(self.country, self.city, self.address)


class OrderItem(models.Model):
    notebook = models.ForeignKey(Notebook, blank=True, null=True, verbose_name='Notebook')
    quantity = models.PositiveIntegerField('Quantity', default=0)
    order = models.ForeignKey(Order, blank=True, null=True, related_name='order_items')

    class Meta:
        verbose_name = 'Order item'
        verbose_name_plural = 'Order items'
