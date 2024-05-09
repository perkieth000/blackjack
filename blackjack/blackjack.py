from random import shuffle
from os import system
from time import sleep
import helper as h

def clear():
    system('clear')

# Define the deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = [(rank, suit) for suit in suits for rank in ranks]

# Function to shuffle the deck
def shuffle_deck():
    global deck
    deck = [(rank, suit) for suit in suits for rank in ranks]
    shuffle(deck)

# Function to deal a card from the deck
def deal_card():
    shuffle_deck()
    return deck.pop()

# Function to calculate the value of a hand
def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    for card in hand:
        rank = card[0]
        if rank.isdigit():
            value += int(rank)
        elif rank in ['Jack', 'Queen', 'King']:
            value += 10
        elif rank == 'Ace':
            value += 11
            num_aces += 1
    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1
    return value

# Function to play the game
def play_game():
    shuffle_deck()
    money = int(input("How much money would you like to bet? "))

    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]
    print(f'Player hand ({calculate_hand_value(player_hand)}):', player_hand)
    print(f'Dealer hand ({dealer_hand[0][0]} + X):', [dealer_hand[0], 'X'])
    while True:
        choice = input('Do you want to hit (h) or stand (s)? ')
        if choice == 'h':
            clear()
            player_hand.append(deal_card())
            print(f'Player hand ({calculate_hand_value(player_hand)}):', player_hand)
            print(f'Dealer hand ({dealer_hand[0][0]} + X):', [dealer_hand[0], 'X'])
            if calculate_hand_value(player_hand) > 21:
                print('Player busts! You lose.')
                h.update_stats(False)
                h.update_money(False, money)
                h.print_stats()
                print(f"Average win rate: {h.get_average_win_rate() * 100:.2f}%")
                print(f"Money: {h.get_money()}")
                break
        elif choice == 's':
            while calculate_hand_value(dealer_hand) < 17: # dealer's turn
                clear()
                print(f'Player hand ({calculate_hand_value(player_hand)}):', player_hand)
                print(f'Dealer hand ({calculate_hand_value(dealer_hand)}):', dealer_hand)
                dealer_hand.append(deal_card())
                sleep(0.75)
            clear()
            print(f'Player hand ({calculate_hand_value(player_hand)}):', player_hand)
            print(f'Dealer hand ({calculate_hand_value(dealer_hand)}):', dealer_hand)
            if calculate_hand_value(dealer_hand) > 21:
                print('Dealer busts! You win.')
                h.update_stats(True)
                h.print_stats()
                h.update_money(True, money)
                h.update_money(False, money)
                print(f"Average win rate: {h.get_average_win_rate() * 100:.2f}%")
                print(f"Money: {h.get_money()}")
            elif calculate_hand_value(dealer_hand) > calculate_hand_value(player_hand):
                print('Dealer wins.')
                h.update_stats(False)
                h.update_money(False, money)
                h.print_stats()
                print(f"Average win rate: {h.get_average_win_rate() * 100:.2f}%")
                print(f"Money: {h.get_money()}")
            elif calculate_hand_value(dealer_hand) < calculate_hand_value(player_hand):
                print('You win.')
                h.update_stats(True)
                h.update_money(True, money)
                h.print_stats()
                print(f"Average win rate: {h.get_average_win_rate() * 100:.2f}%")
                print(f"Money: {h.get_money()}")
            else:
                print('It\'s a tie.')
            break
        else:
            print('Invalid choice. Please try again.')

# Start the game
if __name__ == '__main__':
    while True:
        clear()
        play_game()
        choice = input('Do you want to play again? (y/n) ')
        if not choice.lower().startswith("y"):
            break