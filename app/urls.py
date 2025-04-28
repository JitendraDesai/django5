from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Cars/<int:id>/',views.Cars, name="car"),
    path('home/',views.Home),
    path('about/',views.About),
    path('contact/',views.contact),
    path('service/',views.service),



]