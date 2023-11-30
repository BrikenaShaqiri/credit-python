from cs50 import get_int


def luhn_checksum(card):
    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(card)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0

    checksum += sum(odd_digits)

    for d in even_digits:
        checksum += sum(digits_of(d * 2))

    return checksum % 10


while True:
    card = get_int("Card: ")
    if card > 0:
        break

card_str = str(card)
length = len(card_str)
visa = int(card_str[:1])
amex = int(card_str[:2])
master = int(card_str[:2])

if luhn_checksum(card) == 0:
    if length == 13 and visa == 4:
        print("VISA")
    elif length == 15 and (amex == 34 or amex == 37):
        print("AMEX")
    elif length == 16 and 51 <= master <= 55:
        print("MASTERCARD")
    elif length == 16 and visa == 4:
        print("VISA")
    else:
        print("INVALID")
else:
    print("INVALID")
