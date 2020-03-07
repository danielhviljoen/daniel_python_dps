import random
import string

adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat', 'red',
              'orange', 'yellow', 'green', 'blue', 'purple',
              'fluffy', 'white', 'proud', 'brave']

nouns = ['apple', 'dinosaur','ball', 'toaster', 'goat',
        'dragon', 'hammer', 'duck', 'panda', 'banana', 'teacher', 'tellephone']


print('Welcome to pasword picker')
boolean = True
while boolean == True:
    for num in range(7):
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        number = random.randrange(0, 100)
        special_char = random.choice(string.punctuation)

        password = adjective + noun + str(number) + special_char
        print(password)

    response = input('Would you like more passwords? Type y or n: ')
    if response == 'n':
        boolean = False

