import getpass # for hiding the password while typing
from instaScraper import Scraper 

if __name__ == '__main__':

    print('Enter the username and password of your Instagram Account')
    #username = input('Username: ')
    username = "your_username" # input your username
    #password = getpass.getpass() # input your password
    password = 'your_password'

    print('Enter the username of the target whose photos and descriptions you want to download from')
    '''
        target_username must fulfill either or both of the below two criteria:
        -> You must follow that account
        -> It must be an open account.
    '''
    #target_username = input('Target Username: ') # Enter the username of the account you want to scrap photos and capions from.
    target_username = "target_account"
    scraper = Scraper(username, password, target_username) # Instagram Scraper Object