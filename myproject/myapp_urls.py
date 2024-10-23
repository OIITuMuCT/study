"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin, auth
from django.urls import path, include
from myapp.admin import admin_site
import myapp.views
from django.conf import settings
from django.conf.urls.static import static
from bookr_admin.admin import admin_site

urlpatterns = [
    path("bookradmin/", admin_site.urls),
    path("admin/", admin.site.urls),
    # path("admin/", admin.site.urls),
    path(
        "accounts/", include(("django.contrib.auth.urls", "auth"), namespace="accounts")
    ),
    path(
        "accounts/password_reset/done/",
        auth.views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "accounts/reset/done/", 
        auth.views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete"
    ),
    path("accounts/profile/", myapp.views.profile, name='profile'),
    path("book-search/", myapp.views.book_search, name="book_search"),
    path("", include("myapp.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)