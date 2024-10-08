from django.contrib import admin
from django.contrib.admin import AdminSite

from myapp.models import (Publisher, Contributor, 
                          Book, BookContributor, Review)

class BookrAdminSite(AdminSite):
    title_header = 'Bookr Admin'
    site_header = "Bookr administration"
    index_title = "Bookr site admin"

admin_site = BookrAdminSite(name="bookr")


class BookAdmin(admin.ModelAdmin):
    date_hierarchy = "publication_date"
    list_display = ("title", "isbn13")
    list_filter = ("publisher", "publication_date")
    search_fields = ("title", "isbn", "publisher__name")

    @admin.display(ordering="isbn", description="ISBN-13", empty_value="-/-")
    def isbn13(self, obj):
        """'9780316769174' => '978-0-31-676917-4'"""
        return "{}-{}-{}-{}-{}".format(
            obj.isbn[0:3], obj.isbn[3:4], obj.isbn[4:6], obj.isbn[6:12], obj.isbn[12:13]
        )


def initialled_name(obj):
    """obj.first_names='Jerome David', obj.last_names='Salinger'
    => 'Salinger, JD'"""
    initials = "".join([name[0] for name in obj.first_names.split(" ")])
    return "{}, {}".format(obj.last_names, initials)


class ContributorAdmin(admin.ModelAdmin):
    list_display = ("last_names", "first_names")
    list_filter = ("last_names",)
    search_fields = ("last_names__startswith", "first_names")


class ReviewAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("creator", "book")}),
        ("Review content", {"fields": ("content", "rating")}),
    )


# Register your models here.
admin_site.register(Publisher)
admin_site.register(Contributor, ContributorAdmin)
admin_site.register(Book, BookAdmin)
admin_site.register(BookContributor)
admin_site.register(Review, ReviewAdmin)

