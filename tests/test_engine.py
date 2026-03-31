from src.engine import Card, Rank, Suit, calculate_hand_value


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
    hand = [card1, card2]

    # Act
    hand_value = calculate_hand_value(hand)

    # Assert
    assert hand_value == 20


def test_hand_value_with_ace():
    # Arrange
    card1 = Card(Rank.KING, Suit.SPADES)
    card2 = Card(Rank.FIVE, Suit.HEARTS)
    card3 = Card(Rank.ACE, Suit.HEARTS)
    hand = [card1, card2, card3]

    # Act
    hand_value = calculate_hand_value(hand)

    # Assert
    assert hand_value == 16
