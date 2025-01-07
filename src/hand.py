from src.card import Card

class Hand:
    def __init__(self, card_1: Card = None, card_2: Card = None):
        self.cards = []
        self.add_card(card_1)
        self.add_card(card_2)
        self.card_1 = card_1
        self.card_2 = card_2
    
    def add_card(self, card: Card):
        if len(self.cards) < 2 and card not in self.cards:
            self.cards.append(card)
    
    def get_cards(self) -> list:
        return self.cards
    
    def __str__(self):
        return f"Hand({self.card_1}, {self.card_2})"