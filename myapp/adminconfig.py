from django.contrib.admin.apps import AdminConfig


class MyappAdminConfig(AdminConfig):
    default_site = "admin.BookrAdminSite"
    # default_site = "bookr_admin.admin.BookrAdmin"
