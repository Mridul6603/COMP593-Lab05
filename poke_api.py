#importing requests and working on the script to 
import requests

url_of_poke = 'https://pokeapi.co/api/v2/pokemon/'

def searching_for_poke_ability(Search=''):

    Search = str(Search).strip().lower()

    print ('\n',f'Searching for the Pokemon Ability with the id as inputed {Search}...........', '\n', end='')

    header = {'accept' : 'application/json'}

    
    #Searching the url of the poke in order to collect it's name and ability through the id as inputed by the user.
    searching_the_url = url_of_poke + Search
    
    msg_response = requests.get(searching_the_url, headers=header)

    if msg_response.status_code == requests.codes.ok:
        print('\n','Congratulations, the data has been fetched successfully', '\n')
        return msg_response.json()
    else:
        print('\n','Failure, No such data is available','\n')
        print('\n',f'Error Code : {msg_response.status_code}, Reason For Error : {msg_response.reason}', '\n')
        