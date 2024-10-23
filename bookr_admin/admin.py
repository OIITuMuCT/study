from django.contrib import admin
from django.contrib.auth.admin import User
# from myapp.models import Publisher, Contributor, BookContributor, Book, BookContributor, Review

# Register your models here.
class BookrAdmin(admin.AdminSite):
    site_header = "Bookr Administration"
    site_title = "Bookr"
    index_title = "Bookr site admin"


admin_site = BookrAdmin(name='bookr_admin')
admin_site.register(User)

# admin_site.register(Publisher)
# admin_site.register(Contributor)
# admin_site.register(Book)
# admin_site.register(BookContributor)
# admin_site.register(Review)
