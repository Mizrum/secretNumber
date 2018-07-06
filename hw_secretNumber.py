# Modify the secret number game, such that errors are caught when the users inputs not convertible strings

secret = 40
guess = int(raw_input("Geben Sie eine Zahl ein von 1 bis 100: "))

while secret != "guess":
    print
    if guess > secret:
        print "What a pity, it is too high, please try again."

    elif guess < secret:
        print "Sorry this was not enough, please try it again"

    else:
        print "Congratulation you guessed right ;)"