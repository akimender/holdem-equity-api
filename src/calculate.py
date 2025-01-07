from src.sim import Sim
from src.hand import Hand
from src.river import River
from src.deck import Deck
from src.card import Card
import random

num_iterations = 10000

def get_equity(json_data):
    hand_1 = json_data.get("hand_1")
    hand_2 = json_data.get("hand_2")
    river = json_data.get("river")

    sim = Sim(Hand(json_to_card(hand_1[0]), json_to_card(hand_1[1])),
              Hand(json_to_card(hand_2[0]), json_to_card(hand_2[1])),
              River(list_of_jsons_to_cards(river)))
    
    return run_sim(sim)

def json_to_card(json_data) -> Card:
    return Card(json_data.get("rank"), json_data.get("suit"))

def list_of_jsons_to_cards(json_list: list) -> Hand:
    return [json_to_card(json) for json in json_list]

def run_sim(sim: Sim):
    print("Running " + str(num_iterations) + " simulations")
    num_hand_1_wins = 0
    num_hand_2_wins = 0
    num_ties = 0
    for i in range(num_iterations):
        new_river = get_randomized_full_river(sim.get_deck(), sim.get_river())
        new_sim = Sim(sim.get_hand_1(), sim.get_hand_2(), new_river)
        winning_hand = new_sim.get_winner()
        if winning_hand == sim.get_hand_1():
            num_hand_1_wins += 1
        elif winning_hand == sim.get_hand_2():
            num_hand_2_wins += 1
        else:
            num_ties += 1
    print("Hand 1 wins " + str(num_hand_1_wins*100/num_iterations) + "percent of the time")
    print("Hand 2 wins " + str(num_hand_2_wins*100/num_iterations) + "percent of the time")
    print("Ties happen  " + str(num_ties*100/num_iterations) + "percent of the time")
    return round(num_hand_1_wins*100/num_iterations)

def get_randomized_full_river(deck: Deck, river: list):
    new_river = river.get_copy()
    new_deck = deck.get_shuffled_copy()
    while new_river.get_length() < 5:
        new_river.add_card(new_deck.pop_card())
    return new_river

def create_hand(rank, suit):
    return Hand(rank, suit)