def cards_sum2(hand):
    total_number = 0
    for i in range(0, len(hand)):
        if hand[i] == 2:
            total_number += 2
        elif hand[i] == 3:
            total_number += 3
        elif hand[i] == 4:
            total_number += 4
        elif hand[i] == 5:
            total_number += 5
        elif hand[i] == 6:
            total_number += 6
        elif hand[i] == 7:
            total_number += 7
        elif hand[i] == 8:
            total_number += 8
        elif hand[i] == 9:
            total_number += 9
        elif hand[i] == 10:
            total_number += 10
        elif hand[i] == 'J':
            total_number += 10
        elif hand[i] == 'Q':
            total_number += 10
        elif hand[i] == 'K':
            total_number += 10
        elif hand[i] == 'A':
            total_number += 11
    return total_number