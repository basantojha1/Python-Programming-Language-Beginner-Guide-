import random
print('Hi ! Welcome to the Number guessing Game.')

low = int(input('Enter the Lower Bound:'))
high = int(input('Enter the Higher Bound:'))

print(f"\nYou have 7 chances to guess the number between {low} and {high}. Let's Start !")

num = random.randint(low, high)
ch = 7  # Total Allowed Chance
gc = 0  # Guess Coutner

while gc < ch:
    gc += 1
    guess = int(input('Enter Your Guess:'))

    if guess == num:
        print(f'{guess} is the correct Guess. You guessed it in {gc} attempts.')
        break
    elif gc >=ch and guess != num:
        print(f'Sorry ! The number was {num}. Better luck next time.')

    elif guess > num:
        print('Try a Lower Number')
    
    elif guess < num:
        print('Try a Higher Number')