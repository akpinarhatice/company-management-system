from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

from apps.company.models import DepartmentModel, CompanyModel


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Kullanıcılar bir email adresine sahip olmalıdır.')
        if not username:
            raise ValueError('Kullanıcılar bir kullanıcı adına sahip olmalıdır.')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser):
    first_name = models.CharField(max_length=60, verbose_name='İsim')
    last_name = models.CharField(max_length=100, verbose_name='Soyisim')
    birthday = models.CharField(max_length=10, verbose_name='Doğum Günü')
    email = models.EmailField(max_length=254, verbose_name='Email', unique=True)
    username = models.CharField(max_length=50, unique=True, verbose_name='Kullanıcı Adı')
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(default=True, verbose_name=('Aktiflik'))
    is_admin = models.BooleanField(default=False, verbose_name='Admin')
    is_staff = models.BooleanField(default=False, verbose_name='Çalışan')
    is_superuser = models.BooleanField(default=False, verbose_name=('SuperUser'))
    title = models.CharField(max_length=50, verbose_name='Unvan',blank=True)
    company = models.ForeignKey(CompanyModel, on_delete=models.PROTECT, null=True, blank=True, default=None)
    department = models.ForeignKey(DepartmentModel, on_delete=models.PROTECT, null=True, blank=True, default=None)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = ('Kullanıcı')
        verbose_name_plural = ('Kullanıcılar')
