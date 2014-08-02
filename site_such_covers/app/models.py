# coding: utf-8
from django.db import models


def upload_to(self, filename):
    return 'covers/{}'.format(filename)


class Cover(models.Model):
    title = models.CharField('Title', max_length=255)
    image = models.ImageField('Image', upload_to=upload_to)


class Notebook(models.Model):
    cover = models.ForeignKey(Cover, verbose_name='Cover')
    pages = models.IntegerField('Pages')
