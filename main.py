import requests

name = input('Enter a name you would like to try or type q to quit: ')

while name.lower() != 'q':
    agify_url = 'https://api.agify.io/?name='
    r = requests.get(agify_url + name)
    api_data = r.json()
    print('Name: ' + name)
    print('Times queried:', api_data['count'])
    print('Age guess:', api_data['age'])
    name = input('Enter a name you would like to try or type q to quit: ')
