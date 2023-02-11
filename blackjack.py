import random
import card_counter

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
players_hand = [cards[random.randrange(0, len(cards))], cards[random.randrange(0, len(cards))]]
dealers_hand = [cards[random.randrange(0, len(cards))], cards[random.randrange(0, len(cards))]]


def current_hands():
    print(f"Your hand is: {players_hand}")
    print(f"Dealer's hand is: {dealers_hand}")

dealers_pass = 0
players_pass = 0

def dealers_turn():
    choice = random.random()
    if choice >= 0.5:
        dealers_hand.append(cards[random.randrange(0, len(cards))])
    else:
        global dealers_pass
        dealers_pass += 1
        pass

def players_turn():
    choice = input("Do you want another card? Y/N ")
    if choice == 'Y':
        players_hand.append(cards[random.randrange(0, len(cards))])
    elif choice == 'N':
        global players_pass
        players_pass += 1
        pass
    else:
        print("Excuse me, what was that again?")

current_hands()

while True:
    if card_counter.cards_sum(dealers_hand) == 21 or card_counter.cards_sum(players_hand) > 21:
        print("Dealer won")
        break
    elif card_counter.cards_sum(players_hand) == 21 or card_counter.cards_sum(dealers_hand) > 21:
        print("You won")
        break
    if dealers_pass == 0:
        dealers_turn()
    else:
        pass
    if players_pass == 0:
        players_turn()
    else:
        pass
    if dealers_pass + players_pass == 2:
        if card_counter.cards_sum(dealers_hand) > card_counter.cards_sum(players_hand):
            print("Dealer won")
        elif card_counter.cards_sum(dealers_hand) < card_counter.cards_sum(players_hand):
            print("You won")
        else:
            print("Posh")
            break
current_hands()
