from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('speedometer/', include('speedometer_app.urls')),
]
