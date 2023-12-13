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
                    level9(player)
            elif choice2 == "... am I going crazy?":
                level7(player)
            else:
                print("ERROR!")
        elif choice == "Go for a walk to clean your mind.":
            level17(player)
        else:
            print("ERROR!")


def level4(player):
    """
    Decisiontree level 4
    """
    read_file("./assets/story/4-0-mistake.txt")
    choice = questionary.select(
        "What do you want to do?\n",
        choices=[
            "Investigate.",
            "That's their problem.",
        ]).ask()
    if choice == "Investigate.":
        if player.get_luck() >= 10:
            read_file("./assets/story/4-3-bugfix.txt")
            end(12,"bugfix")
        else:
            read_file("./assets/story/4-5-nofix.txt")
            level16(player)
    elif choice == "That's their problem.":
        level16(player)
    else:
        print("Error in Level 4!")

def level5(player):
    """
    Decisiontree level 5
    """
    read_file("./assets/story/5-0-home.txt")
    choice = questionary.select(
    "What do you want to do?\n",
    choices=[
        "Hide and prepaire for an attack.",
        "Storm and attack!",
    ]).ask()
    if choice == "Hide and prepaire for an attack.":
        if player.get_strength() >=5 :
            level12()
        else:
            level15()
    else:
        level15()


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

def level7(player):
    """
    Decisiontree level 7
    """
    read_file("./assets/story/7-0-crazy.txt")
    choice = questionary.select(
        "What do you want to do?\n\n",
        choices=[
            "Stop and stare at the screen to find a solution.",
            "Keep pressing buttons. Something must work.",
        ]).ask()
    if choice == "Stop and stare at the screen to find a solution.":
        level8(player)
    elif choice == "Keep pressing buttons. Something must work.":
        level9(player)

def level8(player):
    """
    Decisiontree level 8
    """
    read_file("./assets/story/8-0-virtual.txt")
    choice = questionary.select(
        "What do you want to do?\n\n",
        choices=[
            "Move.",
            "Scream!",
        ]).ask()
    if choice == "Move.":
        level18(player)
    elif choice == "Scream!":
        read_file("./assets/story/8-1-friends.txt")
        player.update_fellowship(2)
        choice2 = questionary.select(
            "What do you want to do?\n",
            choices=[
                "Go your own way.",
                "Follow them.",
            ]).ask()
        if choice2 == "Go your own way.":
            read_file("./assets/story/8-2-own-way.txt")
            level18(player)
        elif choice2 == "Follow them.":
            level19(player)
        else:
            print("Error in Level 8!")
    else:
        print("Error in Level 8!")

def level9(player):
    """
    Decisiontree level 9
    """
    read_file("./assets/story/9-0-decisions.txt")
    choice = questionary.select(
        "What do you want to do?\n",
        choices=[
            "Pull the plug!",
            "Press the Power Button.",
        ]).ask()
    if choice == "Pull the plug!":
        if player.get_strength() >= 5:
            read_file("./assets/story/9-1-pull-plug.txt")
            end(5, "Pull the plug!")
        else:
            player.update_strength(-2)
            read_file("./assets/story/9-2-loose.txt")
            choice2 = questionary.select(
                "What do you want to do?\n",
                choices=[
                "Beg for mercy.",
                "RUN!",
            ]).ask()
            if choice2 == "Beg for mercy.":
                level11(player)
            elif choice2 == "RUN!":
                level10(player)
    elif choice == "Press the Power Button.":
        read_file("./assets/story/9-3-power.txt")
        level12(player)
        

def level10(player):
    read_file("./assets/story/10-0-chase.txt")
    choice = questionary.select(
        "What do you want to do?\n",
        choices=[
            "Search your pockets.",
            "Make a fist.",
        ]).ask()
    if choice == "Search your pockets.":
        level14(player)
    elif choice == "Make a fist.":
        read_file("./assets/story/10-1-really.txt")
        choice2 = questionary.select(
        "What do you want to do?\n",
        choices=[
            "I should search my pockets.",
            "Make two fists.",
        ]).ask()
        if choice2 == "I should search my pockets.":
            level14(player)
        elif choice2 == "Make two fists.":
            level13(player)
        else:
            print("Error in Level 10!")
    else:
        print("Error in Level 10!")

def level11(player):
    read_file("./assets/story/11-0-mercy.txt")
    choice = questionary.select(
        "What do you answer?\n",
        choices=[
            "Yes! I've never hurt a soul!",
            "No... To be honest: I suck at life.",
        ]).ask()
    if choice == "Yes! I've never hurt a soul!":
        if player.get(get_fellowship) >= 3:
            read_file("./assets/story/11-1-good.txt")
            end(7, "Angel")
        else:
            read_file("./assets/story/11-1-bad.txt")
            level13(player)
    elif choice == "No... To be honest: I suck at life.":
        read_file("./assets/story/11-1-bad.txt")
        level13(player)
    else:
        print("Error in level 11!")


def level12(player):
    """
    Function to print slowly from text file to console.
    """
    player.update_strength(4)
    read_file("./assets/story/12-0-still.txt")
    choice = questionary.select(
        "What do you want to do?\n",
        choices=[
            "Get ready to attack.",
            "Call the police.",
        ]).ask()
    if choice == "Get ready to attack.":
        read_file("./assets/story/12-1-attack.txt")
        level10(player)
    elif choice == "Call the police.":
        read_file("./assets/story/12-2-police.txt")
        end(6, "1312")

def level13(player):
    read_file("./assets/story/13-0-fist.txt")
    if player.get_strength() >= 5:
        read_file("./assets/story/13-1-strong.txt")
        end(9, "Power Punch!")
    elif player.get_luck() >= 10:
        read_file("./assets/story/13-2-lucky-punch.txt")
        end(10, "Lucky Punch!")
    else:
        read_file("./assets/story/13-3-agency.txt")
        end(11, "Confidentiality Agreement")

def level14(player):
    if player.is_in_inventory("stick"):
        read_file("./assets/story/14-0-stick.txt")
        end(8, "Stick it")
    else:
        level13(player)

def level15(player):
    read_file("./assets/story/15-0-choke.txt")
    choice = questionary.select(
        "What do you want to do?\n",
        choices=[
            "FIGHT BACK!",
            "Nothing. It's over now.",
        ]).ask()
    if choice == "FIGHT BACK!":
        read_file("./assets/story/15-1-fight.txt")
        level14(player)
    elif choice == "Nothing. It's over now.":
        level8(player)
    else:
        print("Error in Level 15!")

def level16(player):
    read_file("./assets/story/4-4-bugreport.txt")
    choice = questionary.select(
        "What is next?\n",
        choices=[
            "Go for a walk and think about the bug.",
            "Next task.",
        ]).ask()
    if choice == "Go for a walk and think about the bug.":
        level17(player)
    elif choice == "Next task.":
        read_file("./assets/story/16-1-task.txt")
        choice2 = questionary.select(
            "What do you want to do?\n",
            choices=[
                "Talk to the computer.",
                "Check the cables.",
            ]).ask()
        if choice2 == "Talk to the computer.":
            if player.get_charisma() >= 6:
                level3(player)
            else:
                level8(player)
        elif choice2 == "Check the cables.":
            level8(player)
        else:
            print("Error in Level 16 - Choice 2")
    else:
        print("Error in Level 16!")

def level17(player):
    read_file("./assets/story/3-4-walk.txt")
    player.update_inventory("stick")
    choice2 = questionary.select(
        "What do you want to do?\n",
        choices=[
            "Go back home.",
            "Stop for a coffee.",
        ]).ask()
    if choice2 == "Go back home.":
        level5(player)
    elif choice2 == "Stop for a coffee.":
        if player.get_luck() >= 5:
            read_file("./assets/story/4-2-coffee-luck.txt")
            end(2, "Coffee Luck")
        else:
            read_file("./assets/story/4-1-coffee.txt")
            level5(player)
    else:
        print("Error in Level 17!")

def level18(player):
    read_file("./assets/story/18-0-desktop.txt")
    end(13, "Print Version")

def level19(player):
    read_file("./assets/story/19-0-town.txt")
    choice = questionary.select(
        "What do you want to do?\n",
        choices=[
            "Charisma.",
            "Strength.",
        ]).ask()
    if choice == "Charisma.":
        read_file("./assets/story/19-1-charisma.txt")
        if player.get_charisma() >= 5:
            read_file("./assets/story/19-2-win.txt")
            end(15, "Win with friends!")
        else:
            level20(player)
    elif choice == "Strength.":
        read_file("./assets/story/19-2-strength.txt")
        if player.get_strength() >= 5:
            read_file("./assets/story/19-3-fight.txt")
            end(16, "Win you freedom.")
        else:
            level20(player)
    else:
        print("Error in Level 19.")

def level20(player):
    read_file("./assets/story/20-0-loss.txt")
    end(14, "You lost the game.")


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
