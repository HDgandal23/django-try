from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('professeur/', views.list_prof),
    path('eleve/', views.list_eleve),
    path('matiere/', views.list_matiere),
    path('niveau/', views.list_niveau),
    path('class/', views.list_classes)
]
