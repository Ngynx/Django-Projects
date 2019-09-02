from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('encuestas/', include('encuestas.urls')),
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
]