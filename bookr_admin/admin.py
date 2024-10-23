from django.contrib import admin
from django.contrib.auth.admin import User


# Register your models here.
class BookrAdmin(admin.AdminSite):
    site_header = "Bookr Administration"
    site_title = "Bookr"
    index_title = "Bookr site admin"


admin_site = BookrAdmin(name='bookr_admin')
admin_site.register(User)

