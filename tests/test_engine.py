from src.engine import Card, Rank, Suit


def test_card():
    # Arrange
    card1 = Card(Rank.ACE, Suit.SPADES)

    # Act
    card_value = card1.rank.value

    # Assert
    assert card_value == 11
