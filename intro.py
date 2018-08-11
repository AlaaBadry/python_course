
print('Hello')

name = input('Who is there? ')

input('Hi ' + name + ', How are you? ')

age = int(input('How old are you? '))

birth_year = 2018 - age

print('So, you were born in', birth_year)

answer = input('Do you want to play a game? ')

while answer != 'yes' and answer != 'ok':
    if answer == 'no':
        answer = input('Why not, just one game? ')
    else:
        answer = input('What did you say? ')

print('Yessss, I love games')

my_num = 35
your_num = int(input('Can you guess the number that I\'m thinking of? '))

while your_num != my_num:
    if your_num < my_num:
        your_num = int(input("I'm thinking in a greater number than that, Enter another one: "))
    else:
        your_num = int(input("I'm thinking in a smaller number than that, Enter another one: "))

print('\nYou got it. Great work')
print('It is a great pleasure to talk with you')
print('\nI have to leave now, Goodbye')
