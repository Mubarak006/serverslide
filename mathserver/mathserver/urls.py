from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('poweroflight/',views.lightpower,name="poweroflight"),
    path('',views.lightpower,name="poweroflightroot")
]
