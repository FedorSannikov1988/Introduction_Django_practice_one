from django.urls import path
from .views import heads_or_tails, \
                   playing_dice, \
                   random_number


urlpatterns = [

    path('heads_or_tails',
         heads_or_tails,
         name='heads_or_tails'),

    path('playing_dice',
         playing_dice,
         name='playing_dice'),

    path('random_number',
         random_number,
         name='random_number'),

]
