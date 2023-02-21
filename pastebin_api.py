import requests

Developer_key = 'gkrsR-ugrrV2ImYL5p1D3_BUvPdzV-S7'
Pastebin_api_url = 'https://pastebin.com/api/api_post.php'

#Main calling function for the title, body, expiration period and publicly listed section
def main():
    url = post_new_paste('title', 'body', '1H',True)
    print(f'New paste URL: {url}')
     
#Pastebin calling 
def post_new_paste(title, body_text, expiration='10M', listed = False):

    #Setup the param for req message
    paste_params = {
        'api_dev_key' : Developer_key,
        'api_option' : 'paste',
        'api_paste_code' : body_text,
        'api_paste_name' : title, 
        'api_paste_expiration_date': expiration,
        'api_paste_private' : 0 if listed else 1
    }

    #send the post req to the pastebin API
    print('Sending POST req t PASTEBIN API')
    resp_msg = requests.post(Pastebin_api_url, data = paste_params)


    #checking whether the POST request was successful
    if resp_msg.ok:
        print('Success')
        return resp_msg.text
    else:
        print('failed')    
        print(f'Status code: {resp_msg.status_code} ({resp_msg.reason})')


if __name__ == '__main__':
    main()