from django.contrib import admin
from django.urls import path, include
from pdf.views import download_file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pdf.urls')),
    path('download/<int:file_id>/', download_file, name='download_file'),
]
