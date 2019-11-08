'''
We will build a guessing game where until the user guesses the Secret word, it will keep on going.
When the user guesses the secret word. He wins.
'''

secret_word = 'atom'
guess = ''
guess_count = 0
total_guess = 3
out_of_guess = False


print('You will get total 3 chances to guess the correct answer.')
print('What is it which is the building block of everything?')
while guess != secret_word and not(out_of_guess):
    if guess_count < total_guess:
        guess = input('Enter your guess: ')
        guess_count += 1
        guess_left = total_guess - guess_count
        if guess_left > 1:
            print('Wrong Guess! You have ' + str(guess_left) +' chances left!')
        elif guess_left == 1:
            print('Wrong Guess! You have ' + str(guess_left) + ' chance left!')
    else:
        out_of_guess = True
if out_of_guess:
    print("You Lose!!!")
else:
    print("You Win!!!")