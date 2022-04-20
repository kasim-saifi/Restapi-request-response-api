from django.contrib import admin
from django.urls import path
from vgoapi.views import*
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',h,name='kasim'),
]
