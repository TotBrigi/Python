secret = 117

guess = int(raw_input("Guess the secret number!"))

if (secret == guess):
    print "Wow, you are awsome!!! This is really the " + str(secret)
else:
    print "Maybe next time! :( This is not " + str(guess)

