from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('tables.urls')),
    path('api/', include('coffee.urls')),
    path('admin/', admin.site.urls),
]
