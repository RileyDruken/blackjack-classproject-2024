import random

def deck_initialize():
    # Creates the deck of cards and shuffles them
    suits = ["Hearts","Clubs","Diamonds","Spades"]
    ranks = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    values = [11,2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    deck = []

    for suit in suits:
        for i in range(len(ranks)):
            deck.append([suit,ranks[i],values[i]])

    random.shuffle(deck)
    return deck


def initialize_game(dealer,player,deck):
    # initializes the game by dealer the cards to the player and dealer
    for i in range(2):
        card = random.choice(deck)
        dealer.append(card)
        deck.remove(card)

        card = random.choice(deck)
        if card[1] == "Ace":
            choice = input("Would you like your Ace to be worth 1? By default, it will be valued at 11. (y/n)")
            if choice.lower == "y":
                card[2] = 1


        player.append(card)
        deck.remove(card)



    print("DEALER's SHOW CARD:")
    print(f"{dealer[0][1]} of {dealer[0][0]}\n")

def calculate_scores(dealer,player):
    dealer_score = 0
    player_score = 0

    for i in dealer:
        dealer_score += i[2]
    for i in player:
        player_score += i[2]

    return dealer_score,player_score

def display_player_cards(player):
    print("YOUR CARDS:")
    for i in player:
        print(f"{i[0]} of {i[1]}")


def main():
    dealer = []
    player = []

    print("BlACKJACK!\nBlackjack payout is 3:2\n")
    deck = deck_initialize()
    initialize_game(dealer,player,deck)
    dealer_score, player_score = calculate_scores(dealer,player)

    display_player_cards(player)











if __name__ == '__main__':
    main()