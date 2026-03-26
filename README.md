# Blackjack

## Introduction

### What is this?

> A terminal-based Blackjack game inspired by the ASCII aesthetic of NetHack.

### Key features

- Payouts are 3:2 (i.e., Play $5 to win $7.50)
- Dealer stands on soft 17 (A + 6)
- After 312 cards (6 52-card decks) are dealt, the shoe is shuffled
- User has the ability to double down and split
  - Will include insurance at a later time
- User has the ability to increase and decrease bet size (min: $1, max: $100)

## Installation

```bash
git clone https://github.com/marleomac3/Blackjack.git
cd Blackjack
python -m venv .venv # assuming you have Python installed
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Running the game

```bash
python src/game.py
```
