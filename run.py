# import google auth and spreadsheet libaries
import gspread
from google.oauth2.service_account import Credentials
from player import Player

# Setting up global variables to work with google sheets
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('workfromhome')

endings = SHEET.worksheet('endings')

# ----------------------------------------------------------- #


def welcome():
    """
    Printing the Welcome message at the beginning of each game on the screen
    """
    found_endings, number_endings = get_endings()
    print("Welcome to 'work from home' a story telling game that takes you on a journey in your virtual home.")
    print("You will habe to make decisions that effect your story and takes you on different paths.")
    print("Try to find as many ending as possible.")
    print("You have found " + str(found_endings) + " of " + str(number_endings) + " endings so far.")
    print("-------------------------------------")


def get_endings():
    """
    Getting the endings the user already found.
    """
    data = endings.get_all_values()
    found_endings = 0
    number_endings = 0

    for data in data:
        number_endings += 1

        if data[1] == "TRUE": 
            found_endings += 1
    
    return found_endings, number_endings

def delete():
    """
    Delete the current score by setting all endings to false.
    """
    print("...deleting your score...")
    data = endings.get_all_values()
    i = 1

    for item in data:
        endings.update_cell(i, 2, 'FALSE')
        i += 1

    print("Your score has been deleted.")


def play():
    print("Let's play!")



def main():
    """
    Base function running the game.
    """
    # Initial Player object is created
    player = Player(0, 0, 0, 0, [])

    welcome()
    print("Type 'start', to start the game with your current score.")
    print("Type 'delete', to delete your score and start from scratch.")
    game = input()
    if game == "delete":
        print("Are you sure you want to delete your current score?")
        delete_check = input("[Type 'YES' to delete your score:]")
        if delete_check == "YES":
            delete()
        else:
            print("Your score has NOT been deleted.")
    elif game == "start":
        play()



# Making sure the script is run directly
if __name__ == "__main__":
    main()
