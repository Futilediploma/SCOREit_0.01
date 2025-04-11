# your_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('leagues/', include ('leagues.urls')),
    path('teams/', include ('teams.urls')),
]
