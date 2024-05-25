from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("hisse/<str:id>", views.hisse, name="hisse"),
    path("doviz/<str:id>", views.doviz, name="doviz"),
    path("altin/<str:id>", views.altin, name="altin"),
    path("bist/<str:id>", views.bist, name="bist"),
]