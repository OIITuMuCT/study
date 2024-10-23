from django.contrib import admin
from django.contrib.auth.admin import User
from django.template.response import TemplateResponse
from django.urls import path


# Register your models here.
class BookrAdmin(admin.AdminSite):
    site_header = "Bookr Administration"
    site_title = "Bookr"
    index_title = "Bookr site admin"
    logout_template = 'admin/logout.html'



admin_site = BookrAdmin(name='bookr_admin')
admin_site.register(User)

class SysAdminSite(admin.AdminSite):
    def system_health_dashboard(self, request):
        request.current_app = self.name
        context = self.each_context(request)
        # View function logic
        return context

    def get_urls(self):
        base_urls = super().get_urls() # get the existing set of URLs
        #Define our URL patterns for custom views
        urlpatterns = [
            path("health_dashboard/", self.system_health_dashboard)
        ]
        return base_urls + urlpatterns # Return the update mapping 