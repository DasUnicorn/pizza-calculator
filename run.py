import questionary
import time
# import google auth and spreadsheet libaries
import gspread
from google.oauth2.service_account import Credentials
# import local class
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
    print_picture("./assets/story/pc.txt")
    slow_print("Welcome to WORK FROM HOME a story telling game that takes you on a journey through a turbulent Home Office Day.\n")
    slow_print("Your decisions affect the story and the end of your day.\n")
    slow_print("Try to find as many ending as possible.\n")
    check_score()
    print("\n-------------------------------------\n")

def check_score():
    """
    Checks the number of endings found and the number of endings in total.
    """
    found_endings, number_endings = get_endings()
    slow_print("You have found " + str(found_endings) + " of " + str(number_endings) + " endings so far.\n")

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
    slow_print("\n...deleting your score...\n")
    data = endings.get_all_values()
    i = 1

    for item in data:
        endings.update_cell(i, 2, 'FALSE')
        i += 1

    slow_print("Your score has been deleted.\n")


def play(player):
    """
    The start of the gameplay that divert in the storylines
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

def level2(player):
    """
    Decisiontree level 2
    """
    read_file("./assets/story/2-0-call.txt")
    choice = questionary.select(
    "What do you want to do?\n",
    choices=[
        "I am focused now, they can send me an e-mail.",
        "Take the call.",
    ]).ask()

    if choice == "I am focused now, they can send me an e-mail.":
        read_file("./assets/story/2-2-lunch.txt")
        choice2 = questionary.select(
            "What do you want to do?\n",
            choices=[
                "Grab a Snack and go for a walk.",
                "Cook a meal while watching learning videos about presentation skills.",
            ]).ask()
        if choice2 == "Grab a Snack and go for a walk.":
            player.update_strength(2)
        elif choice2 == "Cook a meal while watching learning videos about presentation skills.":
            player.update_charisma(2)
        else:
            print("ERROR!")

        level4(player)

    elif choice == "Take the call.":
        read_file("./assets/story/2-1-help.txt")
        choice2 = questionary.select(
            "What do you want to do?\n",
            choices=[
                "Help the colleague.",
                "Decline and focus on your own work.",
            ]).ask()
        if choice2 == "Help the colleague.":
            player.update_fellowship(2)
        elif choice2 == "Decline and focus on your own work.":
            player.update_fellowship(-2)
        else:
            print("ERROR!")

        level3(player)
    else:
        print("ERROR!")


def level3(player):
    """
    Decisiontree level 3
    """
    read_file("./assets/story/3-0-problem.txt")
    if player.get_fellowship() >= 3:
        read_file("./assets/story/3-1-solved.txt")
        end(1, "'What a great day working from home.'")
    else:
        read_file("./assets/story/3-2-worse.txt")
        player.update_luck(-2)
        choice = questionary.select(
            "What do you want to do?\n",
            choices=[
                "Start talking to the computer.",
                "Go for a walk to clean your mind.",
            ]).ask()
        if choice == "Start talking to the computer.":
            read_file("./assets/story/3-3-talk.txt")
            choice2 = questionary.select(
            "Wait ... \n",
            choices=[
                "... is this morse-code?",
                "... am I going crazy?",
            ]).ask()
            if choice2 == "... is this morse-code?":
                if (player.get_fellowship >= 3) or (player.get_luck >= 5):
                    level6(player)
                else: 
                    level7(player)
            elif choice2 == "Stop by a a coffee.":
                level7(player)
            else:
                print("ERROR!")
        elif choice == "Go for a walk to clean your mind.":
            read_file("./assets/story/3-4-walk.txt")
            player.update_inventory("stick")
            choice2 = questionary.select(
            "What do you want to do?\n",
            choices=[
                "Go back home.",
                "Stop by a a coffee.",
            ]).ask()
            if choice2 == "Go back home.":
                level5(player)
            elif choice2 == "Stop by a a coffee.":
                if player.get_luck() >= 5:
                    read_file("./assets/story/4-2-coffee-luck.txt")
                    end(2, "Coffee Luck")
                else:
                    read_file("./assets/story/4-1-coffee.txt")
                    level5(player)
            else:
                print("ERROR!")
        else:
            print("ERROR!")


def level4(player):
    """
    Decisiontree level 4
    """
    print("YEAH! LEVEL 4!") #--------------------------------------------------------------------#

def level5(player):
    """
    Decisiontree level 5
    """
    pass #---------------------------------------------------------------------------------------#

def level6(player):
    """
    Decisiontree level 6
    """
    read_file("./assets/story/6-0-code.txt")
    choice = questionary.select(
    "This is the moment to ...\n",
    choices=[
        "... take advantage of the situation.",
        "... become friends with the machine.",
    ]).ask()
    if choice == "... become friends with the machine.":
        read_file("./assets/story/6-2-friendship.txt")
        end(3, "Humans and Machines")
    elif choices == "... take advantage of the situation.":
        read_file("./assets/story/6-1-deal.txt")
        choice2 = questionary.select(
        "What do you want to do?\n\n",
        choices=[
            "Make the deal.",
            "Decline offer and talk further.",
        ]).ask()
        if choice2 == "Make the deal.":
            read_file("./assets/story/6-3-make-deal.txt")
            end(4, "quid pro quo")
        else:
            read_file("./assets/story/6-4-bridge.txt")
            read_file("./assets/story/6-2-friendship.txt")
            end(3, "Humans and Machines")

def slow_print(text):
    """
    Function to print slowly from text file to console.
    """
    for char in text:
        print(char, end = "", flush = True)
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
    Displays the "end" ascii art, number and name of ending, saves the ending found.
    """
    read_file("./assets/story/end.txt")
    slow_print("Congratulations!\n You found Ending number " + str(number) + " titled " + text + ".")
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
    Saves the given entry to the google sheet
    """
    slow_print("...saving your the ending...")
    endings.update_cell(number, 2, 'TRUE')
    slow_print("Ending has been saved.")

def main():
    """
    Base function running the game.
    """
    #One game run is one loop
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
    
        if choice == "Delete the current score":
            delete_check =questionary.confirm("Are you sure you want to delete your current score?", default=False).ask()
            if delete_check:
                delete()
            else:
                slow_print("Your score has NOT been deleted.")
        elif choice == "Start the game":
            play(player)
        else:
            break;

# Making sure the script is run directly
if __name__ == "__main__":
    main()
