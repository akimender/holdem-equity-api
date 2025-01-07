from src.card import Card
from src.hand import Hand
from src.river import River
import random
import copy

class Deck:
    def __init__(self, cards=None):
        self.cards = cards if cards is not None else []
        self.generate_new_deck()

    # sets cards to a new shuffled Deck of cards
    def generate_new_deck(self):
        self.cards.clear()
        for i in range(1, 14): # i in 1-13
            self.cards.append(Card(i, "Spades"))
            self.cards.append(Card(i, "Clubs"))
            self.cards.append(Card(i, "Diamonds"))
            self.cards.append(Card(i, "Hearts"))
        random.shuffle(self.cards)

    def pop_card(self) -> Card:
        return self.cards.pop()
    
    def add_card(self, card: Card):
        self.cards.append(card)
    
    def get_all_cards(self) -> list:
        return self.cards
    
    def remove_card(self, card: Card):
        self.cards.remove(card)

    def remove_hand_cards(self, hand: Hand):
        for card in hand.get_cards():
            self.cards.remove(card)
    
    def remove_river_cards(self, river: River):
        for card in river.get_cards():
            if card in self.cards:
                self.cards.remove(card)

    def shuffle_cards(self):
        random.shuffle(self.cards)
        return self

    def get_shuffled(self):
        deck = Deck(self.cards)
        return deck.shuffle_cards()
    
    def get_shuffled_copy(self):
        deep_copy = copy.deepcopy(self).get_shuffled()
        return deep_copy