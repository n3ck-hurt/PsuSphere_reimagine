from django.contrib import admin
from django.urls import path, include
from .views import service_worker

urlpatterns = [
    path("admin/", admin.site.urls),
    path("service-worker.js", service_worker, name="service-worker"),
    path("accounts/", include("allauth.urls")), # allauth routes
    path("", include("pwa.urls")),
    path("", include("studentorg.urls")),
]

