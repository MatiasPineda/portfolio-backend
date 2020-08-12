from datetime import datetime
import pytz
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView

from .models import Deck, Card

tz = pytz.timezone('America/Santiago')


class DeckListView(ListView):
    model = Deck
    template_name = 'deck_list.html'
    context_object_name = 'all_deck_list'


class DeckUpdateView(UpdateView):
    model = Deck
    fields = ('name',)
    template_name = 'deck_update.html'
    context_object_name = 'deck_update'
    success_url = reverse_lazy('deck_list')


class DeckCreateView(CreateView):
    model = Deck
    fields = ('name',)
    template_name = 'deck_create.html'
    success_url = reverse_lazy('deck_list')


class DeckDeleteView(DeleteView):
    model = Deck
    template_name = 'deck_delete.html'
    success_url = reverse_lazy('deck_list')


class CardListView(ListView):
    model = Card
    template_name = 'card_list.html'
    context_object_name = 'card_list'

    def get_queryset(self):
        return super().get_queryset().filter(deck_id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['deck'] = Deck.objects.get(pk=self.kwargs['pk'])
        context['deck'] = get_object_or_404(Deck, pk=self.kwargs['pk'])
        return context


class CardCreateView(CreateView):
    model = Card
    fields = ('front', 'back',)
    template_name = 'card_create.html'

    def get_success_url(self):
        return reverse('card_list', args=[self.object.deck_id])

    def form_valid(self, form):
        form.instance.deck_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CardCreateView, self).get_context_data(**kwargs)
        context['deck_name'] = get_object_or_404(Deck, pk=self.kwargs['pk'])
        return context


class CardUpdateView(UpdateView):
    model = Card
    fields = ('deck', 'front', 'back',)
    template_name = 'card_update.html'

    def get_success_url(self):
        return reverse('card_list', args=[self.object.deck_id])


class CardDeleteView(DeleteView):
    model = Card
    template_name = 'card_delete.html'

    def get_success_url(self):
        return reverse('card_list', args=[self.object.deck_id])


class FlashcardFrontView(DetailView):
    model = Card
    template_name = 'flashcard_front.html'


class FlashcardBackView(DetailView):
    model = Card
    template_name = 'flashcard_back.html'

    def get_object(self, queryset=None):
        card = super().get_object(queryset)
        card.last_looked_at = datetime.now(tz)
        card.save()
        return card
