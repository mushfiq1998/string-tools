from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('reverse/', views.reverse_string, name='reverse_string'),
    path('split/', views.split_string, name='split_string'),
    path('join/', views.join_string, name='join_string'),
    path('sort/', views.sort_string, name='sort_string'),
    path('slice/', views.slice_string, name='slice_string'),
    path('lower2upper/', views.lower2upper, name='lower2upper'),
    path('upper2lower/', views.upper2lower, name='upper2lower'),
    path('remove_duplicate_words/', views.remove_duplicate_words, name='remove_duplicate_words'),
    path('numbers2words/', views.numbers2words, name='numbers2words'),
    path('sentence_counter/', views.sentence_counter, name='sentence_counter'),
]