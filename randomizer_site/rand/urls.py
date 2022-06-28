from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.show_all_topics, name='show_all_topics'),
    path('add/', views.add_topic, name='add_topic'),
    path('just_added/', views.just_added, name='just_added'),
    path('random/', views.random, name='random')
]
