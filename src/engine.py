from collections import namedtuple
from enum import Enum


class Rank(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 10
    QUEEN = 10
    KING = 10
    ACE = 11


class Suit(Enum):
    SPADES = "♠"
    HEARTS = "♥"
    DIAMONDS = "♦"
    CLUBS = "♣"


Card = namedtuple("Card", ["rank", "suit"])

class Hand:
    def __init__(self):
        self.cards: list[Card] = []

    def add_card(self, card: Card):
        self.cards.append(card)

    def total(self):

        value = 0
        aces = 0

        for card in self.cards:
            value += card.rank.value
            if card.rank == Rank.ACE:
                aces += 1

        while value > 21 and aces > 0:
            value -= 10
            aces -= 1

        return value
