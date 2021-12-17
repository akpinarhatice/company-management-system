from django.db import models
from django.db.models import CASCADE

from apps.inheritance.inheritance import BaseModel, AdressModel, ContactModel


class DepartmentModel(ContactModel):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ('Departman')
        verbose_name_plural = ('Departmanlar')

    def __str__(self):
        return self.name


class CompanyModel(AdressModel, ContactModel):
    name = models.CharField(max_length=100)
    logo = models.ImageField(blank=True, verbose_name='Logo')
    shortname = models.CharField(max_length=20, verbose_name='Kısatılmış İsim')

    class Meta:
        verbose_name = ('Şirket')
        verbose_name_plural = ('Şirketler')

    def __str__(self):
        return self.shortname


class WorkingModel(models.Model):
    WORKING_TYPES = [
        ('sh', 'shift'),
        ('over', 'overtime shift'),
        ('rm', 'remote')]
    user = models.ForeignKey("accounts.UserModel", on_delete=CASCADE)
    working_type = models.CharField(max_length=50, choices=WORKING_TYPES, default='sh', verbose_name='Çalışma Türü')
    starting_time = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Başlangıç Saati')
    ending_time = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Bitiş Saati')
    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_total_working_time(self):
        return self.ending_time - self.starting_time

    class Meta:
        verbose_name = ('Çalışma')
        verbose_name_plural = ('Çalışmalar')
