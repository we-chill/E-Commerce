from io import BytesIO
from datetime import date
from PIL import Image

from django.db import models
from django.core.files import File
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.slug}/'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True)
    category = models.ForeignKey(Category, related_name='products', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=99.99)
    description = models.TextField(null=True, blank=True)
    origin = models.CharField(max_length=200, null=True, blank=True)
    warranty_expired_date = models.DateField(null=True, blank=True, default=date(2099, 12, 31))
    status = models.PositiveSmallIntegerField(null=True, blank=True, default=100)
    # image = models.ImageField(upload_to='images/', blank=True, null=True)
    # thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        category = self.category.title.strip().replace(' ', '')
        title = self.title.strip().replace(' ', '')
        return 'http://127.0.0.1:8000/media/images/' + category + '/' + title + '.jpg/'

    # def get_image(self):
    #     if self.image:
    #         return 'http://127.0.0.1:8000' + self.image.url
    #     return ''

    # def get_thumbnail(self):
    #     if self.thumbnail:
    #         return 'http://127.0.0.1:8000' + self.thumbnail.url
    #     else:
    #         if self.image:
    #             self.thumbnail = self.make_thumbnail(self.image)
    #             self.save()
    #             return 'http://127.0.0.1:8000' + self.thumbnail.url
    #         else:
    #             return ''

    # def make_thumbnail(self, image, size=(300, 200)):
    #     img = Image.open(image)
    #     img.convert("RGB")
    #     img.thumbnail(size)

    #     thumb_io = BytesIO()
    #     img.save(thumb_io, 'JPEG', quality=85)

    #     thumbnail = File(thumb_io, name=image.name.replace('images/', ''))

    #     return thumbnail
