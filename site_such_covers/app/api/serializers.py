# coding: utf-8
from __future__ import unicode_literals
from rest_framework import serializers
from site_such_covers.app.models import Cover, Notebook
from django.core.files.base import ContentFile
import base64


class CoverSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.SerializerMethodField('get_image')

    class Meta:
        model = Cover
        fields = ['title', 'image']

    def get_image(self, obj):
        if self.init_data and self.init_data.has_key('image'):
            image_data = self.init_data.get('image')
            if isinstance(image_data, basestring) and image_data.startswith('data:image'):
                format, imgstr = image_data.split(';base64,')
                ext = format.split('/')[-1]
                obj.image = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
                obj.save()

        if self.init_files and self.init_files.has_key('image'):
            obj.image = self.init_files['image']
            obj.save()

        if obj.image:
            return '/media/{}'.format(obj.image)
        return ''


class NotebookSerializer(serializers.HyperlinkedModelSerializer):
    cover = CoverSerializer(source='cover', required=True)

    class Meta:
        model = Notebook
        fields = ['cover', 'pages']
