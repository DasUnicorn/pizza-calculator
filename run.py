# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def welcome():
    """
    Printing the Welcome message at the beginning of each game on the screen
    """
    print("                    _       __                       _                           ")
    print("                   | |     / _|                     | |                          ")
    print("__      _____  _ __| | __ | |_ _ __ ___  _ __ ___   | |__   ___  _ __ ___   ___  ")
    print("\ \ /\ / / _ \| '__| |/ / |  _| '__/ _ \| '_ ` _ \  | '_ \ / _ \| '_ ` _ \ / _ \ ")
    print(" \ V  V / (_) | |  |   <  | | | | | (_) | | | | | | | | | | (_) | | | | | |  __/ ")
    print("  \_/\_/ \___/|_|  |_|\_\ |_| |_|  \___/|_| |_| |_| |_| |_|\___/|_| |_| |_|\___| ")
    print("---------------------------------------------------------------------------------")
    print("")
    print("Welcome to 'work from home' a story telling game that takes you on a journey in your virtual home.")
    print("You will habe to make decisions that effect your story and takes you on different paths.")
    print("Try to find as many ending as possible.")


def main():
    """
    Base function running the game.
    """
    welcome()


# Making sure the script is run directly
if __name__ == "__main__":
    main()
