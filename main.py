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

def initialize_game(deck):
    dealer = []
    player = []

    # Initializes the game by dealing the cards to the player and dealer
    for i in range(2):
        card = deck.pop()
        dealer.append(card)

        card = deck.pop()
        player.append(card)
    print("\nDEALER's SHOW CARD:")
    print(f"{dealer[0][1]} of {dealer[0][0]}\n")

    return  dealer, player

def calculate_score_player(player):
    #calculates scores
    player_score = 0

    for i in player:
        player_score += i[2]
    return player_score

def calculate_score_dealer(dealer):
    #calculates score
    dealer_score = 0

    for i in dealer:
        dealer_score += i[2]
    return dealer_score

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
    if player_score < 21:
        print(f"YOUR POINTS:\t {player_score}")
        print(f"DEALER'S POINTS: {dealer_score}\n")
    else:
        print(f"YOUR POINTS:\t {player_score}")

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


def dealer_turn(dealer, deck):
    dealer_score = 0

    # Draw cards until the dealer's score reaches 17 or higher
    while dealer_score < 17:
        card = deck.pop()
        dealer.append(card)
        # Calculate the dealer's score after drawing each card
        for i in dealer:
            dealer_score += i[2]
    return dealer_score

def place_bet():
    money = float(db.read_money())
    print(f"Money: {money}")
    while True:
        try:
            bet_amount = float(input("Bet amount: "))
            if 5 <= bet_amount <= money and bet_amount <= 1000:
                break
            else:
                print("Invalid bet amount")
        except ValueError:
            print("Invalid input for bet amount try again.")
    return bet_amount, money

def play_again():
    while True:
        player_choice = input("Play again? (y/n): ").lower()
        if player_choice == "y" or player_choice == "n":
            break
        print("Invalid input! please try again")
    if player_choice == "y":
        return False
    else:
        return True

def main():
    print("BlACKJACK!\nBlackjack payout is 3:2\n")

    while True:
        deck = deck_initialize()
        bet_amount, money = place_bet()
        dealer, player = initialize_game(deck)
        display_player_cards(player)

        while True:
            player_score = calculate_score_player(player)
            if player_score > 21:
                # dealer score 0 cause dealer score is not needed when player bust since they lose any ways dealer turn is skipped
                display_dealer_cards(dealer)
                display_player_cards(player)

                win_check(0,player_score,bet_amount,money)
                break

            choice = input("Hit or stand? (hit/stand): ").lower()
            if choice == "hit":
                card = deck.pop()
                player.append(card)
                display_player_cards(player)

            elif choice == "stand":

                print()

                dealer_score = dealer_turn(dealer, deck)
                display_dealer_cards(dealer)
                win_check(dealer_score, player_score, bet_amount, money)
                break

            else:
                print("invalid choice please try again!")
        if play_again():
            break
    print("\nCome back soon!\nBye!")


if __name__ == '__main__':
    main()