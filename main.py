import random
import db

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


def initialize_game(dealer, player, deck, money):
    # Initializes the game by dealing the cards to the player and dealer
    for i in range(2):
        card = deck.pop()
        ace_check(card, 0, 0, True)
        dealer.append(card)

        card = deck.pop()
        ace_check(card,0,0,False)
        player.append(card)

    deck = deck_initialize()
    money = float(db.read_money())


    print("\nDEALER's SHOW CARD:")
    print(f"{dealer[0][1]} of {dealer[0][0]}\n")
    return money

def calculate_scores(dealer,player):
    #calculates scores
    dealer_score = 0
    player_score = 0

    for i in dealer:
        dealer_score += i[2]
    for i in player:
        player_score += i[2]

    return dealer_score,player_score

def display_player_cards(player):
    # displays player cards
    print("YOUR CARDS:")
    for i in player:
        print(f"{i[1]} of {i[0]}")
    print()

def display_dealer_cards(dealer):
    # displays dealer cards
    print("DEALER CARDS:")
    for i in dealer:
        print(f"{i[0]} of {i[1]}")
    print()

def win_check(dealer_score, player_score,bet_amount,money):
    # checks if the winner
    print(f"YOUR POINTS:\t {player_score}")
    print(f"DEALER'S POINTS: {dealer_score}")

    if player_score == 21:
        print("Congrats, You Win.")
        money += bet_amount * 1.5
    elif player_score > 21:
        print("Player bust, you lose.")
        money -= bet_amount
    elif player_score > dealer_score:
        print("Congrats, You Win.")
        money += bet_amount * 1.5
    elif player_score == dealer_score:
        print("Draw, it is a tie.")
    elif dealer_score > 21:
        print("Dealer bust, you win.")
        money += bet_amount * 1.5
    else:
        print("Sorry, you lose.")
        money -= bet_amount

    money = round(money, 2)
    print("Money: ", money)
    db.write_money(str(money))

def ace_check(card, player_score, dealer_score, is_dealer=False):
    #checks if the card the player or dealer has is an ace
    if card[1] == "Ace":
        if is_dealer:
            if dealer_score + 11 > 21:
                card[2] = 1
            else:
                card[2] = 11
        else:
            if player_score + 11 > 21:
                card[2] = 1
            else:
                while True:
                    choice = input("Would you like your Ace to be worth 1? By default, it will be valued at 11. (y/n): ").lower()
                    print()
                    if choice == "y":
                        card[2] = 1
                        break
                    elif choice == "n":
                        card[2] = 11
                        break
                    else:
                        print("Invalid choice. Please try again.")

def dealer_turn(dealer, deck, dealer_score, player):
    # makes the dealer play their turn
    while dealer_score < 17:
        card = deck.pop()
        ace_check(card,0,dealer_score,True)

        dealer.append(card)
        dealer_score, player_score = calculate_scores(dealer, player)
    return dealer_score

def main():
    dealer = []
    player = []

    money = float(db.read_money())
    print("BlACKJACK!\nBlackjack payout is 3:2\n")

    deck = deck_initialize()
    print(f"Money: {money}")

    while True:
        try:
            bet_amount = float(input("Bet amount: "))
            if bet_amount >= 5 and bet_amount <= 1000 and bet_amount <= money:
                break
            else:
                print("Invalid bet amount")
        except ValueError:
            print("Invalid input for bet amount try again.")
    initialize_game(dealer, player, deck, money)


    display_player_cards(player)

    while True:

        dealer_score, player_score = calculate_scores(dealer, player)

        if player_score > 21:
            win_check(dealer_score,player_score,bet_amount,money)
            while True:
                player_choice = input("Play again? (y/n): ").lower()
                if player_choice == "y" or player_choice == "n":
                    break
                print("Invalid input! please try again")
            if player_choice != "y":
                break
            print()
            # resets values for new game
            dealer = []
            player = []
            initialize_game(dealer, player, deck,money)
            display_player_cards(player)

        choice = input("Hit or stand? (hit/stand): ").lower()

        if choice == "hit":
            card = deck.pop()
            ace_check(card,player_score,dealer_score,False)

            player.append(card)
            display_player_cards(player)

        elif choice == "stand":
            dealer_score = dealer_turn(dealer, deck, dealer_score, player)

            print()
            display_dealer_cards(dealer)

            #check if winner
            win_check(dealer_score, player_score,bet_amount,money)

            #sees if the player wants to end the game
            while True:
                player_choice = input("Play again? (y/n): ").lower()
                if player_choice == "y" or player_choice == "n":
                    break
                print("Invalid input! please try again")
            if player_choice != "y":
                break
            print()

            money = float(db.read_money())
            print("Money:", money)
            while True:
                try:
                    bet_amount = float(input("Bet amount: "))
                    if bet_amount >= 5 and bet_amount <= 1000 and bet_amount <= money:
                        break
                    else:
                        print("Invalid bet amount")
                except ValueError:
                    print("Invalid input for bet amount try again.")
            # resets values for new game
            dealer = []
            player = []
            initialize_game(dealer, player, deck, money)

            display_player_cards(player)

        else:
            print("invalid choice please try again!")


    print("\nCome back soon!\nBye!")


if __name__ == '__main__':
    main()