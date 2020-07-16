from django.urls import path
from .views import DownloadMovie

urlpatterns = [
    path('', DownloadMovie.as_view(), name='home')
]