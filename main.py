import random

def deck_initialize():
    suits = ["Hearts","Clubs","Diamonds","Spades"]
    values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    deck = []

    for i in suits:
        for x in values:
            deck.append([i,x])

    random.shuffle(deck)

    return deck


def main():
    deck = deck_initialize()
    print(deck)


if __name__ == '__main__':
    main()