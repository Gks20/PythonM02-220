# variable for guessed number
guess_me = 5

# for numbers in range of 10
for number in range(10):
    # if number is lower than 5, print 'too low'
    if number < guess_me:
        print('too low')
# if number is equal to 5, print 'found it!', then break loop
    elif number == guess_me:
        print('found it!')
        break
# if number is greater than 5, print 'oops' then break loop
    elif number > guess_me:
        print('oops')
        break
