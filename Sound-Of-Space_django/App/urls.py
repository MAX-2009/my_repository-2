from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = "App"

urlpatterns = [
    path("", views.index, name="index"),
    path('earth', views.about, name='earth'),
    path('moon', views.eng, name='moon'),
    path('solar', views.lol, name='solar'),
    path('star', views.star, name='star'),

]
