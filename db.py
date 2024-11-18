

def write_money(money):
    with open("money.txt", "w") as file:
        file.write(money)


def read_money():
    money = 0
    try:
        with open("money.txt") as file:
            for line in file:
                money = line
    except OSError:
        money = 100.0
    return money


def main():
    print(read_money())

if __name__ == '__main__':
    main()