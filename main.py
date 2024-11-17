import random

def deck_initialize():
    # Creates the deck of cards and shuffles them
    suits = ["Hearts","Clubs","Diamonds","Spades"]
    ranks = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    values = [[1,11],2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

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
        player.append(card)
        deck.remove(card)



def main():
    print("BlACKJACK!\nBlackjack payout is 3:2\n")
    deck = deck_initialize()
    print(deck)

    dealer = []
    player = []











if __name__ == '__main__':
    main()