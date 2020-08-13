from django.urls import path
from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('decks/', DeckListView.as_view(), name='deck_list'),
    path('decks/new/', DeckCreateView.as_view(), name='deck_create'),
    path('decks/<int:pk>/', DeckUpdateView.as_view(), name='deck_update'),
    path('decks/<int:pk>/delete/', DeckDeleteView.as_view(), name='deck_delete'),
    path('cards/<int:pk>/front/', FlashcardFrontView.as_view(), name='flashcard_front'),
    path('cards/<int:pk>/back/', FlashcardBackView.as_view(), name='flashcard_back'),

    path('decks/<int:pk>/cards/', CardListView.as_view(), name='card_list'),
    path('decks/<int:pk>/cards/new/', CardCreateView.as_view(), name='card_create'),
    path('cards/<int:pk>/', CardUpdateView.as_view(), name='card_update'),
    path('cards/<int:pk>/delete/', CardDeleteView.as_view(), name='card_delete'),
]