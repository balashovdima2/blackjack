#kaartide suvaliseks valimiseks vajalik, põhimõtteliselt peatab kaartide lugemise,
#sest ta võib võtta ühe mängu ajal mitu sama kaarti
#decke on põhimõtteliselt lõpmatu arv
import random

#defineerime kaartide mastid ja numbrid, anname numbritele blackjacki väärtused

suits = ['Ärtu', 'Ruutu', 'Risti', 'Poti']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

#kaardi võtmise funktsioon, tagastab suvalise masti ja suvalise numbri ennikuna, mis on pmst kaart

def get_card():
    rank = random.choice(ranks)
    suit = random.choice(suits)
    return (rank, suit)

#käe väärtuse arvutamise funktsioon, teeb ässad automaatselt ühtedeks kui muidu oleks bust

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

#mängu peamine funktsioon, mäng ise

def play_round(balance):
    print("\n=== UUS RAUND ===")
    print("Saldo:", balance)

#panuse suuruse sisestamine

    while True:
        try:
            bet = int(input("Sisesta panuse suurus: "))
            if 1 <= bet <= balance:
                break
            print("Ebasobiv suurus.")
        except ValueError:
            print("Sisesta number.")

#kaartide võtmine, süsteem jätab need meelde listi

    player_hand = [get_card(), get_card()]
    dealer_hand = [get_card(), get_card()]

#näitab kaarte, mängjal mõlemat, majal vaid ühte

    while True:
        print("\nSinu käsi:", player_hand, "=>", calc_value(player_hand))
        print("Majal on:", dealer_hand[0])

#blackjacki saamine

        if calc_value(player_hand) == 21:
            print("Blackjack! Võitsid 1.5-kordse panuse.")
            return balance + int(bet * 1.5)

#hitimise ja standimise kood

        action = input("Hit või Stand? (H/S): ").upper()
        if action == 'H':
            player_hand.append(get_card())
            if calc_value(player_hand) > 21:
                print("\nSinu käsi:", player_hand, "=>", calc_value(player_hand))
                print("Bust! Sa kaotasid.")
                return balance - bet
        elif action == 'S':
            break

#maja terve käsi (koos teise kaardiga)

    print("\nMaja näitab:", dealer_hand, "=>", calc_value(dealer_hand))

#maja standib 17 peal, hitib kui alla 17

    while calc_value(dealer_hand) < 17:
        dealer_hand.append(get_card())
        print("Maja hitib:", dealer_hand, "=>", calc_value(dealer_hand))

#käte lõppväärtused

    player_value = calc_value(player_hand)
    dealer_value = calc_value(dealer_hand)

    print("\nLõplikud käed:")
    print("Sinu käsi:", player_hand, "=>", player_value)
    print("Maja käsi:", dealer_hand, "=>", dealer_value)

#mängu lõppseis võit, kaotus, viik

    if dealer_value > 21 or player_value > dealer_value:
        print("Sa võitsid!")
        return balance + bet
    elif dealer_value > player_value:
        print("Maja võitis.")
        return balance - bet
    else:
        print("Viik, panus tagastatud sulle.")
        return balance

#mängu algus

def main():
#saad valida oma algussaldo 
    print("=== BLACKJACK ===")
    balance = int(input("Sisesta algussaldo: "))
#näitab algussaldot
    print("=== BLACKJACK ===")
    print("Algussaldo:", balance)

#uue käe alustamine, toimib alguses ja ka mängu keskel

    while balance > 0:
        start = input("\nJaga uus käsi? (Y/N): ").upper()
        if start == 'Y':
            balance = play_round(balance)
        else:
            print("Väljun mängust...")
            break

#lõplik kaotus, viskab mängust välja

    if balance <= 0:
        print("Sul on raha otsas, mäng läbi.")

#mängu alustamine koodis

if __name__ == '__main__':
    main()