from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path


class BookrAdminSite(admin.AdminSite):
    title_header = "Bookr Admin"
    site_header = "Bookr Administration Portal"
    index_title = "Bookr site admin"