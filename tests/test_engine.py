from src.engine import Card, Rank, Suit, Hand


def test_card():
    # Arrange
    card1 = Card(Rank.ACE, Suit.SPADES)

    # Act
    card_value = card1.rank.value

    # Assert
    assert card_value == 11


def test_hand_value():
    # Arrange
    card1 = Card(Rank.KING, Suit.SPADES)
    card2 = Card(Rank.KING, Suit.HEARTS)
    hand = Hand()
    hand.add_card(card1)
    hand.add_card(card2)

    # Act
    hand_value = hand.total()

    # Assert
    assert hand_value == 20


def test_hand_value_with_ace():
    # Arrange
    card1 = Card(Rank.KING, Suit.SPADES)
    card2 = Card(Rank.FIVE, Suit.HEARTS)
    card3 = Card(Rank.ACE, Suit.HEARTS)
    hand = Hand()
    hand.add_card(card1)
    hand.add_card(card2)
    hand.add_card(card3)

    # Act
    hand_value = hand.total()

    # Assert
    assert hand_value == 16
