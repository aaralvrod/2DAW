from django.urls import path

from . import views

app_name = 'creatures'

urlpatterns = [
    path('', views.creatures_list, name='creatures-list'),
    path('<creature_slug>/', views.creature_detail, name='creature-detail'),
]
