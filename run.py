import questionary
import time
# import google auth and spreadsheet libaries
import gspread
from google.oauth2.service_account import Credentials
# import local class
from player import Player
from level import *

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
    Printing the Welcome message and current score on the screen
    """
    print_picture("./assets/story/pc.txt")
    slow_print(
        "Welcome to WORK FROM HOME a story telling game" +
        " that takes you on a journey through a turbulent Home Office Day.\n"
    )
    slow_print("Your decisions affect the story and the end of your day.\n")
    slow_print("Try to find as many ending as possible, " +
               "or just enjoy your run.\n"
               )
    check_score()
    print("\n-------------------------------------\n")


def check_score():
    """
    Checks the number of endings found and the number of endings in total.
    """
    found_endings, number_endings = get_endings()
    slow_print(
        "You have found " +
        str(found_endings) +
        " of " +
        str(number_endings) +
        " endings so far.\n")


def get_endings():
    """
    Getting the endings the user already found from the google sheet.
    """
    data = endings.get_all_values()
    found_endings = 0
    number_endings = 0

    for item in data:
        number_endings += 1

        if item[1] == "TRUE":
            found_endings += 1

    return found_endings, number_endings


def delete():
    """
    Delete the current score by setting all endings
    in the Google Sheet to false.
    """
    slow_print("\n...deleting your score...\n")
    data = endings.get_all_values()
    i = 1

    for item in data:
        endings.update_cell(i, 2, 'FALSE')
        i += 1

    slow_print("Your score has been deleted.\n")


def play(player):
    """
    The start of the gameplay that divert in different storylines.
    """
    print_picture("./assets/story/sun.txt")
    read_file("./assets/story/1-0-good-morning.txt")

    choice = questionary.select(
        "What do you want to do?\n",
        choices=[
            "Joining the optional morning stand up.",
            "A pre-office workout.",
            "Taking a nap.",
            "Chatting with colleagues"
        ]).ask()

    if choice == "Joining the optional morning stand up.":
        player.set_stats(5, 2, 2, 4)
        read_file("./assets/story/1-1-standup.txt")
    elif choice == "A pre-office workout.":
        player.set_stats(3, 5, 1, 4)
        read_file("./assets/story/1-2-workout.txt")
    elif choice == "Taking a nap.":
        player.set_stats(1, 1, 10, 1)
        read_file("./assets/story/1-3-nap.txt")
    elif choice == "Chatting with colleagues":
        player.set_stats(2, 3, 3, 5)
        read_file("./assets/story/1-4-chat.txt")
    else:
        print("ERROR!")

    level2(player)


def slow_print(text):
    """
    Function to print slowly from text to console.
    """
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.03)


def print_picture(txt_file):
    """
    Function to print from txt file to console.
    """
    with open(txt_file) as file:
        file_text = file.read()
        print(file_text + "\n")


def read_file(story_file):
    """
    Function to print slowly from txt file to console.
    """
    with open(story_file) as file:
        file_text = file.read()
        slow_print(file_text + "\n")


def end(number, text):
    """
    Displays the "end" ascii art, number and name of ending,
    and saves the ending found.
    The user gets asked if the want to restart or exit.
    """
    read_file("./assets/story/end.txt")
    slow_print("Congratulations!\n You found Ending number " +
               str(number) + " titled " + text + ".\n")
    save_ending(number)
    check_score()
    choice = questionary.select(
        "And now?",
        choices=[
            "Restart the game!",
            "Enough for today. Exit program.",
        ]).ask()

    if choice == "Enough for today. Exit program.":
        exit()


def save_ending(number):
    """
    Saves the given entry to the google sheet.
    """
    slow_print("...saving your the ending...")
    endings.update_cell(number, 2, 'TRUE')
    slow_print("Ending has been saved.")


def main():
    """
    Base function running the game.
    """
    # One game run is one loop
    while True:
        # Initial Player object is created
        player = Player(0, 0, 0, 0, [])

        welcome()
        choice = questionary.select(
            "What do you want to do?",
            choices=[
                "Start the game",
                "Delete the current score",
                "End the game"
            ]).ask()

        # Deleting
        if choice == "Delete the current score":
            delete_check = questionary.confirm(
                "Are you sure you want to delete your current score?",
                default=False).ask()
            if delete_check:
                delete()
            else:
                slow_print("Your score has NOT been deleted.")
        # Start the game
        elif choice == "Start the game":
            play(player)
        # End game
        else:
            break


# Making sure the script is run directly
if __name__ == "__main__":
    main()
