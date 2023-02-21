from pastebin_api import post_new_paste
from sys import argv
from poke_api import searching_for_poke_ability


#defining the main function in order to call and search for the list and ability of pokemon 

def main():
    Search = argv[1]


    dict_poke = searching_for_poke_ability(Search)

#searching and printing out the url
    
    if dict_poke:
        paste_title = get_title_for_paste(Search)

        body_paste = get_body_for_paste(dict_poke)

        url_paste = post_new_paste(paste_title, body_paste, '1W')

        print(url_paste)


def get_body_for_paste(dict_poke):

    pokemon_list = [" - "+p['ability']['name'] for p in dict_poke['abilities']]
    
    print(pokemon_list)
    
    body_paste = '\n'.join(pokemon_list)
    return body_paste
    
def get_title_for_paste(Search):
    return f'Information has been provided on the Pokemon {Search}'

main()