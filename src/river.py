from src.card import Card
import copy

class River:
    def __init__(self, cards: Card=[]):
        self.cards = cards

    def add_card(self, card: Card):
        self.cards.append(card)

    def get_cards(self) -> list:
        return self.cards
    
    def get_copy(self):
        return copy.deepcopy(self)
    
    def get_length(self):
        return len(self.cards)