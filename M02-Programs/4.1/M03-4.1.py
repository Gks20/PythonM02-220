# variable for guess
guess = 8

# variable for secret number
secret = 5

# if guess is lower than secret, print too low.
if guess < secret:
    print('too low.')
# if guess is greater than secret, print too high.
elif guess > secret:
    print('too high.')
# if guess is equal to secret, print just right.
else:
    print('just right.')
