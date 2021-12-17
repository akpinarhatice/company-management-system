from django.db import models


class AdressModel(models.Model):
    neighborhood = models.CharField(max_length=50, verbose_name='Mahalle')
    street = models.CharField(max_length=50, verbose_name='Cadde')
    district = models.CharField(max_length=50, verbose_name='İlçe')
    city = models.CharField(max_length=50, verbose_name='Şehir')
    country = models.CharField(max_length=50, verbose_name='Ülke')
    number = models.CharField(max_length=50, verbose_name='No')
    description = models.CharField(max_length=100, verbose_name='Açıklama')

    class Meta:
        abstract = True


class ContactModel(models.Model):
    phone = models.CharField(max_length=20, verbose_name='Telefon Numarası', blank=True)
    fax_no = models.CharField(max_length=200, verbose_name='Fax Numarası', blank=True)
    email = models.EmailField(max_length=200, verbose_name='Email Adresi', blank=True)

    class Meta:
        abstract = True


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
