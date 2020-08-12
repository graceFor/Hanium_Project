from django.contrib import admin
from django.urls import path, include
import plantapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', plantapp.views.index, name='index'),
]
