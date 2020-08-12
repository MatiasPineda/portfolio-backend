from django.db import models


class Deck(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    def next_card(self):
        return self.cards.earliest('last_looked_at')


class Card(models.Model):
    deck = models.ForeignKey(
        Deck,
        on_delete=models.CASCADE,
        related_name='cards'
    )
    front = models.TextField()
    back = models.TextField()
    last_looked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        dots = "" if len(self.front)<30 else "..."
        return f'{self.front[:30]}{dots}'