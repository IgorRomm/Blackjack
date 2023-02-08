import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10]
players_hand = [cards[random.randrange(0, len(cards))], cards[random.randrange(0, len(cards))]]
dealers_hand = [cards[random.randrange(0, len(cards))], cards[random.randrange(0, len(cards))]]


def current_hands():
    print(f"Your hand is: {players_hand}")
    print(f"Dealer's hand: {dealers_hand}")


def dealers_turn():
    choice = random.random()
    if choice >= 0.5:
        dealers_hand.append(cards[random.randrange(0, len(cards))])
    else:
        pass


def players_turn():
    choice = input("Do you want another card? Y/N ")
    if choice == 'Y':
        players_hand.append(cards[random.randrange(0, len(cards))])
    elif choice == 'N':
        pass
    else:
        print("Excuse me, what was that again?")


def cards_sum(hand):
    total_number = 0
    for card in hand:
        total_number += card
    return total_number

current_hands()

while True:
    if cards_sum(dealers_hand) > 21 or cards_sum(players_hand) == 21:
        print("You won")
        break
    elif cards_sum(players_hand) > 21 or cards_sum(dealers_hand) == 21:
        print("Dealer won")
        break
    else:
        dealers_turn()
        players_turn()
        current_hands()