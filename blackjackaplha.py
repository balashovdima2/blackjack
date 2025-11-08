import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

def get_card():
    rank = random.choice(ranks)
    suit = random.choice(suits)
    return (rank, suit)


def calc_value(hand):
    total = 0
    aces = 0
    for rank, suit in hand:
        total += values[rank]
        if rank == 'A':
            aces += 1
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

def game():
    print("=== BLACKJACK ===")
    
    player_hand = []
    dealer_hand = []
    
    player_hand.append(get_card())
    dealer_hand.append(get_card())
    
    print("Your card:", player_hand)
    print("Dealer's card:", dealer_hand)
    
    player_value = calc_value(player_hand)
    dealer_value = calc_value(dealer_hand)
    
    print("Your points:", player_value)
    print("Dealer's points:", dealer_value)    
    
    
def main():
    balance = 500
    print("Your balance:", balance)
    
    start = input('Start the game? (Y/N): ').upper()
    if start == 'Y':
        game()
    else:
        print("Okay, exiting the game...")
    

if __name__ == '__main__':
    main()

