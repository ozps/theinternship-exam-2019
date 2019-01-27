import random

print('Select Category:')
print('1. Animals')
print('2. Colors')
print('3. Mobile Phone Brands')

category = -1
words = []
scores = 0
remain = 10
correct = False

while(category == -1):
    temp = int(input('Enter a number: '))
    category = temp if temp == 1 or temp == 2 or temp == 3 else -1

if category == 1:
    words = [line.rstrip('\n') for line in open('words/animals.txt')]
    hints = [line.rstrip('\n') for line in open('words/animals_hint.txt')]
elif category == 2:
    words = [line.rstrip('\n') for line in open('words/colors.txt')]
    hints = [line.rstrip('\n') for line in open('words/colors_hint.txt')]
elif category == 3:
    words = [line.rstrip('\n') for line in open('words/mobile_brands.txt')]
    hints = [line.rstrip('\n')
             for line in open('words/mobile_brands_hint.txt')]
else:
    words = []
    hints = []

rand_idx = random.randint(0, len(words)-1)
real_word = words[rand_idx]
hint_word = hints[rand_idx]
guess_word = real_word
wrong_guess = []

for x in real_word:
    if x.isalpha():
        guess_word = guess_word.replace(x, '_ ', 1)
    else:
        guess_word = guess_word.replace(x, x + ' ', 1)

print('\nHint:', hint_word)
print('Guess Word:', guess_word)

while(remain != 0 and not correct):
    print()
    guess = input('Guess: ').strip()
    remain -= 1
    temp = ''
    for i in range(len(real_word)):
        if real_word[i].lower() == guess.lower() and real_word[i].lower() not in guess_word.lower():
            temp += real_word[i] + ' '
            scores += 5
        else:
            if guess.lower() not in wrong_guess and guess.lower() not in real_word.lower():
                wrong_guess.append(guess.lower())
            temp += guess_word[2*i] + ' '
    guess_word = temp
    correct = True if guess_word.replace(' ', '') == real_word else False
    print('Guess Word:', guess_word)
    print('Scores: ', scores)
    print('Guess Remaining:', remain)
    if len(wrong_guess) > 0:
        print('Wrong Guess:', ' '.join(wrong_guess))
if correct:
    scores += 100
    print('\nGenius! The word is', guess_word.replace(' ', '') + '.')
    print('Bonus scores: 100')
    print('You got', scores, 'scores.')
else:
    print('\nNot completed! The word is', real_word + '.')
    print('Your guess word is', guess_word + '.')
    print('You got', scores, 'scores.')
