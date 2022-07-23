from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.show_all_topics, name='show_all_topics'),
    path('add/', views.add_topic, name='add_topic'),
    path('just_added/', views.just_added, name='just_added'),
    path('random/', views.random, name='random'),
    path('all/<int:id>/', views.get_topic_info, name='topic_info'),
    path('all/<int:id>/remove', views.confirm_remove, name='confirm_remove'),
    path('all/<int:id>/remove/deleted', views.remove_topic, name='deleted'),
    path('all/<int:id>/edit', views.edit_topic, name='edit_topic')
]
