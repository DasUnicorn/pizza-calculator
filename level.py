from run import *


def level2(player):
    """
    The logic and decision tree that displays the given text
    and manges the input option of Level 2.
    """
    read_file("./assets/story/2-0-call.txt")
    choice = questionary.select(
        "What do you want to do?\n",
        choices=[
            "Take the call.",
            "I am focused now, they can send me an e-mail.",
        ]).ask()

    if choice == "I am focused now, they can send me an e-mail.":
        read_file("./assets/story/2-2-lunch.txt")
        choice2 = questionary.select(
            "What do you want to do?\n",
            choices=[
                "Grab a Snack and go for a walk.",
                "Cook a meal while watching learning videos" +
                " about presentation skills.",
            ]).ask()
        if choice2 == "Grab a Snack and go for a walk.":
            player.update_strength(2)
            read_file("./assets/story/2-5-snack.txt")
        elif choice2 == ("Cook a meal while watching learning videos" +
                         " about presentation skills."):
            player.update_charisma(2)
            read_file("./assets/story/2-4-videos.txt")
        else:
            print("Error in Level 2, option 1.")

        level4(player)

    elif choice == "Take the call.":
        read_file("./assets/story/2-1-help.txt")
        choice2 = questionary.select(
            "What do you want to do?\n",
            choices=[
                "Decline and focus on your own work.",
                "Help the colleague.",
            ]).ask()
        if choice2 == "Help the colleague.":
            player.update_fellowship(2)
            read_file("./assets/story/2-3-help.txt")
        elif choice2 == "Decline and focus on your own work.":
            player.update_fellowship(-2)
        else:
            print("Error in Level 2, option 2.")

        level3(player)
    else:
        print("Error in Level 2!")


def level3(player):
    """
    The logic and decision tree that displays the given text
    and manges the input option of Level 3.
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
            level21(player)
        elif choice == "Go for a walk to clean your mind.":
            level17(player)
        else:
            print("Error in Level3!")


def level4(player):
    """
    The logic and decision tree that displays the given text
    and manges the input option of Level 4.
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
            end(12, "bugfix")
        else:
            read_file("./assets/story/4-5-nofix.txt")
            level16(player)
    elif choice == "That's their problem.":
        level16(player)
    else:
        print("Error in Level 4!")


def level5(player):
    """
    The logic and decision tree that displays the given text
    and manges the input option of Level 5.
    """
    read_file("./assets/story/5-0-home.txt")
    choice = questionary.select(
        "What do you want to do?\n",
        choices=[
            "Hide and prepaire for an attack.",
            "Storm and attack!",
        ]).ask()
    if choice == "Hide and prepaire for an attack.":
        if player.get_strength() >= 5:
            level12(player)
        else:
            level15(player)
    elif choice == "Storm and attack!":
        level15(player)
    else:
        print("Error in Level 5!")


def level6(player):
    """
    The logic and decision tree that displays the given text
    and manges the input option of Level 6.
    """
    read_file("./assets/story/6-0-code.txt")
    choice = questionary.select(
        "This is the moment to ...\n",
        choices=[
            "... become friends with the machine.",
            "... take advantage of the situation.",
        ]).ask()
    if choice == "... become friends with the machine.":
        read_file("./assets/story/6-2-friendship.txt")
        end(3, "Humans and Machines")
    elif choice == "... take advantage of the situation.":
        read_file("./assets/story/6-1-deal.txt")
        choice2 = questionary.select(
            "What do you want to do?\n\n",
            choices=[
                "Decline offer and talk further.",
                "Make the deal.",
            ]).ask()
        if choice2 == "Make the deal.":
            read_file("./assets/story/6-3-make-deal.txt")
            end(4, "quid pro quo")
        elif choice2 == "Decline offer and talk further.":
            read_file("./assets/story/6-4-bridge.txt")
            read_file("./assets/story/6-2-friendship.txt")
            end(3, "Humans and Machines")
        else:
            print("Error in Level 6, option 2.")
    else:
        print("Error in Level 6!")


def level7(player):
    """
    The logic and decision tree that displays the given text
    and manges the input option of Level 7.
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
        read_file("./assets/story/7-1-buttons.txt")
        level9(player)
    else:
        print("Error in Level 7!")


def level8(player):
    """
    The logic and decision tree that displays the given text
    and manges the input option of Level 8.
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
            print("Error in Level 8, option 2!")
    else:
        print("Error in Level 8!")


def level9(player):
    """
    The logic and decision tree that displays the given text
    and manges the input option of Level 9.
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
            else:
                print("Error in Level 9, option 1!")
    elif choice == "Press the Power Button.":
        read_file("./assets/story/9-3-power.txt")
        level12(player)
    else:
        print("Error in Level 9!")


def level10(player):
    """
    The logic and decision tree that displays the given text
    and manges the input option of Level 10.
    """
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
            print("Error in Level 10 - option 2!")
    else:
        print("Error in Level 10!")


def level11(player):
    """
    The logic and decision tree that displays the given text
    and manges the input option of Level 11.
    """
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
    The logic and decision tree that displays the given text
    and manges the input option of Level 12.
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
    else:
        print("Error in Level 12")


def level13(player):
    """
    The logic and decision tree that displays the given text
    and manges the input option of Level 13.
    """
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
    """
    The logic and decision tree that displays the given text
    and manges the input option of Level 14.
    """
    if player.is_in_inventory("stick"):
        read_file("./assets/story/14-0-stick.txt")
        end(8, "Stick it")
    else:
        level13(player)


def level15(player):
    """
    The logic and decision tree that displays the given text
    and manges the input option of Level 15.
    """
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
    """
    The logic and decision tree that displays the given text
    and manges the input option of Level 16.
    """
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
                "Throw your face into your hands and start mumbling.",
                "Check the cables.",
            ]).ask()
        if choice2 == "Throw your face into your hands and start mumbling.":
            if player.get_charisma() >= 6:
                level21(player)
            else:
                level8(player)
        elif choice2 == "Check the cables.":
            level8(player)
        else:
            print("Error in Level 16 - Choice 2")
    else:
        print("Error in Level 16!")


def level17(player):
    """
    The logic and decision tree that displays the given text
    and manges the input option of Level 17.
    """
    read_file("./assets/story/3-4-walk.txt")
    player.update_inventory("stick")
    choice2 = questionary.select(
        "What do you want to do?\n",
        choices=[
            "Stop for a coffee.",
            "Go back home.",
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
    """
    The Text that is displayed in Level 18.
    """
    read_file("./assets/story/18-0-desktop.txt")
    end(13, "Print Version")


def level19(player):
    """
    The logic and decision tree that displays the given text
    and manges the input option of Level 19.
    """
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
    """
    The Text that is displayed in Level 20.
    """
    read_file("./assets/story/20-0-loss.txt")
    end(14, "You lost the game.")


def level21(player):
    """
    The logic and decision tree that displays the given text
    and manges the input option of Level 21.
    """
    read_file("./assets/story/3-3-talk.txt")
    choice2 = questionary.select(
        "Wait ... \n",
        choices=[
            "... is this morse-code?",
            "... am I going crazy?",
        ]).ask()
    if choice2 == "... is this morse-code?":
        if (player.get_fellowship() >= 3) or (player.get_luck() >= 5):
            level6(player)
        else:
            read_file("./assets/story/3-5-noway.txt")
            level9(player)
    elif choice2 == "... am I going crazy?":
        level7(player)
    else:
        print("Error in Level 3, option 1!")
