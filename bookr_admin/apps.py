from django.apps import AppConfig


class BookrAdminConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    default_site = 'bookr_admin.admin.BookrAdmin'
    name = "bookr_admin"
