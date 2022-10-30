'''
Program:        Query Game
Author:         Joshua DeLawter-Gourlay
Description:    This is a program that calls the Agify API that when queried with a name, returns a guestimate of your age and
                the number of times that word has been queried. The main purpose of the API is the game guessing mechanic, but
                I propose we should turn it into a game. The API has been used so many times that even things like my own last
                name ('Gourlay') has been queried 5 times. My challenge to you is to find the highest and lowest queries of real
                objects or names that you can.
'''

import requests

# initialize some counting variables to make a game
count_min = 9999999999
min_name = ''
count_max = 0
max_name = ''

print()
name = input('Enter a name you would like to try or type q to quit: ')

while name.lower() != 'q':
    if name.lower() == 's':
        print(f'Current maximum best score is {max_name} with {count_max} queries.')
        print(f'Current minimum best score is {min_name} with {count_min} queries.')
        print()
        name = input('Enter a name you would like to try, type q to quit, or s to view your best scores: ')
        continue
    agify_url = 'https://api.agify.io/?name='
    r = requests.get(agify_url + name)
    api_data = r.json()
    if api_data['count'] == None:
        api_data['count'] = 0
    print('Name: ' + name)
    print('Times queried:', api_data['count'])
    print('Age guess:', api_data['age'])
    if api_data['count'] < count_min:
        count_min = api_data['count']
        min_name = api_data['name']
        print('Congratuations! You found a new min!')
    if api_data['count'] > count_max:
        count_max = api_data['count']
        max_name = api_data['name']
        print('Congratulations! You found a new max!')
    print()
    name = input('Enter a name you would like to try, type q to quit, or s to view your best scores: ')
print(f'Final maximum best score is {max_name} with {count_max} queries.')
print(f'Final minimum best score is {min_name} with {count_min} queries.')