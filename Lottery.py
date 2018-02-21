import random

def generate_lottery_numbers(how_many_numbers):
    lottery = []

    while True:
        if len(lottery) == how_many_numbers:
           break
        lottery_numbers = random.randint(1, 100)

        if lottery_numbers not in lottery:
            lottery.append(lottery_numbers)

    return lottery


def main():

    print "Welcome to the Lottery numbers generator."

    question = raw_input(" Please enter how many random numbers would you like to have: ")
    try:
        question_number = int(question)
        print generate_lottery_numbers(question_number)
    except ValueError:
        print "I need a number!"

    print "END"

if __name__ == "__main__":
    main()