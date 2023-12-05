# import google auth and spreadsheet libaries
import questionary
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
    read_file("./assets/story/pc.txt")
    slow_print("Welcome to WORK FROM HOME a story telling game that takes you on a journey through a turbulent Home Office Day.")
    slow_print("Your decisions affect the story and the end of your day.")
    print("Try to find as many ending as possible.")
    check_score()
    print("-------------------------------------\n")

def check_score():
    found_endings, number_endings = get_endings()
    print("You have found " + str(found_endings) + " of " + str(number_endings) + " endings so far.")

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


def play(player):
    read_file("./assets/story/sun.txt")
    read_file("./assets/story/1-0-good-morning.txt")

    choice = questionary.select(
    "What do you want to do?",
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
    read_file("./assets/story/2-0-call.txt")
    choice = questionary.select(
    "What do you want to do?",
    choices=[
        "I am focused now, they can send me an e-mail.",
        "Take the call.",
    ]).ask()

    if choice == "I am focused now, they can send me an e-mail.":
        read_file("./assets/story/2-2-lunch.txt")
        choice2 = questionary.select(
            "What do you want to do?",
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
            "What do you want to do?",
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
    read_file("./assets/story/3-0-problem.txt")
    if player.get_fellowship() >= 3:
        read_file("./assets/story/3-1-solved.txt")
        end(1, "'What a great day working from home.'")
    else:
        read_file("./assets/story/3-2-worse.txt")

def level4(player):
    print("YEAH! LEVEL 4!")

def read_file(story_file):
    """
    Function to open, read, print and close
    story files to console.
    """
    with open(story_file) as file:
        file_text = file.read()
        print(file_text + "\n")

def end(number, text):
    read_file("./assets/story/end.txt")
    print("Congratulations!\n You found Ending number " + str(number) + " titled " + text + ".")
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
    print("...saving your the ending...")
    endings.update_cell(number, 2, 'TRUE')
    print("Ending has been saved.")

def main():
    """
    Base function running the game.
    """

    #One run is one loop
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
                print("Your score has NOT been deleted.")
        elif choice == "Start the game":
            play(player)
        else:
            break;



# Making sure the script is run directly
if __name__ == "__main__":
    main()
