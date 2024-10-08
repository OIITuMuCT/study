from django.contrib.admin.apps import AdminConfig


class MyappAdminConfig(AdminConfig):
    default_site = "admin.BookrAdminSite"
