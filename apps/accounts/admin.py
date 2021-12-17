from django.contrib import admin

from apps.accounts.models import UserModel


class UserList(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name',
                    'is_active')
    list_display_links = ('username', 'first_name', 'last_name')
    list_filter = ('username', 'first_name', 'last_name'
                   )
    search_fields = ('username', 'first_name', 'last_name'
                     )
    list_per_page = 10


admin.site.register(UserModel, UserList)
