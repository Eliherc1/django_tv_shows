from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio),
    path('shows', views.shows),
    path('shows/new/', views.add_show),
    path('shows/create', views.crear_show),
    path('shows/<int:num>', views.ver_show),
    path('shows/<int:num>/delete', views.eliminar_show),
    path('shows/<int:num>/edit', views.editar_show) ,
    #path('shows/<int:num>/update', views.update_show) ,
]
