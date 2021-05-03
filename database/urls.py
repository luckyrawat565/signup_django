from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('src/',include('src.urls')),
    path('',include('src.urls'))
]
