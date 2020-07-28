from django.contrib import admin
from django.urls import path
import plantapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', plantapp.views.home, name='home'),
]
