#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

def main():
    secret = random.randint(0,20)
    life = 3
    score = 0
    new_game = "yes"

    while life>0 and new_game == "yes":
        guess = int(raw_input("Guess the secret number between 0 and 20!"))

        if (secret == guess):
            print "Wow, you are awsome!!! This is really the " + str(secret)
            break
        elif (secret > guess):
            print "It is bigger!"
        elif (secret < guess):
            print "It is smaller!"
        if (secret != guess):
            life -= 1
            score -= 1
            print "Life: " + str(life)
            print "Score: " + str(score)
        else:
            life += 1
            score +=1
            print "Life: " + str(life)
            print "Score: " + str(score)
        if life == 0:
            print "This was my secret number: " + str(secret)
            print "Good bye!"


if __name__ == "__main__":
    main()