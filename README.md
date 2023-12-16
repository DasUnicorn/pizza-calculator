# "Work from Home" - Story Telling Game
"Work from home" is an interactive storytelling game where players take on the role of the protagonist in a dynamic narrative. The game can be played in the console or in a virtual console in the web-browser.
The game is centered around your first remote office day, where every choice you make influences the storyline and leads to different outcomes. Try to find as many endings as possible.

Read below to learn how to deploy the game youself or check out the [live-site](https://murmuring-peak-78506-458d466df584.herokuapp.com/).

![Mock up](/assets/img/readme/mock-up.png)

--- 

# Content

<!-- toc -->


---

## Technologies Used

* GitHub – code storage
* Sublime Text - Editor
* Heroku - Deployment

### Languages Used

Python
(HTML and JavaScript from deployment template)

### Frameworks, Libraries & Programs Used

Github
(NodeJS from deployment template)

## User Experience

### Target Audience
The taget audience are people who enjoy interactive storytelling and decision-based games.
Due to the content of the story I advice a minumum age of 14 years to play along.
This game can be played as a casual gamer, who prefer games that can be played in shorter sessions and do not require a significant time commitment, or excessively to find all possible endings.

### User stories

#### As a New Player:
##### I want clear instructions on how to make choices
* So that I can navigate the story easily, even if I'm not familiar with console-based games.

##### I want a straightforward and intuitive interface
* So that I can easily navigate the game without complex controls.

#### For the game play:
##### I want a compelling and immersive narrative
* So that I can feel engaged and invested in the story.

##### I want my choices to have significant consequences
* So that my decisions feel impactful and meaningful.

##### I want to see the immediate and long-term effects of my decisions
* So that I can learn from my choices and adapt my strategy accordingly.

##### I want to know how many possible endings there are 
* So that I can strive to experience every outcome and complete the game fully.

##### I want to know how many endings I have found
* So that I can be happy about my achivement.


## Design

### Story and Inspiration
In creating the game, my aim was to craft a narrative that starts with a familiar scenario, gradually evolving into an increasingly intricate fantasy realm that rapidly intensifies in complexity and imagination.
I took inspiration from [Choose Your Own Adventure](https://en.wikipedia.org/wiki/Choose_Your_Own_Adventure) Books where the palyer is *"making choices that determine the main character's actions and the plot's outcome"*, as well as the indie game ["Papers, Please"](https://en.wikipedia.org/wiki/Papers,_Please). *"The game has a scripted story mode with twenty possible endings depending on the player's actions"* 

### Flowchart
One of the most challenging aspects was maintaining a clear overview of the story and its various plotlines. so it was necessary to create an extensive flowchart to document the progression. Each element within these flowcharts is designated with a star, serving as a marker to indicate the implementation level of the corresponding code (for example objects marked with the star and the number 8 are implemented in the function "level8(player)").
The preview of the board can be seen below. The [full Miro board](https://miro.com/app/board/uXjVNHT1bqI=/?share_link_id=87020844922) can be inspected online.

![Miro Board](/assets/img/readme/miro.png)

### Gameplay
The game operates in the following manner: Users engage by making decisions, and in the background, a player object of the player class undergoes updates based on these choices. The player's character can experience growth or decline in stats, contingent on the decisions made. Additionally, the narrative takes divergent paths according to these choices. To achieve particular endings or storylines, players must have specific stats. Each player possesses an inventory where they can collect items, adding an extra layer of depth to the game.

![Player Class](/assets/img/readme/player.png)

The player stats are never shown directly to the player and instead written into the story.
While playing the player has to guess if they are strong or otherwise capable enough to undergo different options and the text gives them hints through their journey like "You feel stronger now", or "You are lucky and found ..." to have a sense about their own strengths.
This way it isn't obvious what choices are best to make and leaves the player to watch out for story clues.

### questionary
To make user interaction more user friendly and minimize input errors, the ["questionary"](https://questionary.readthedocs.io/en/stable/) library was integrated into the game.
This allows users to navigate through options using arrow keys and select their choice with the Enter key.
The use of "questionary" serves as a robust error prevention mechanism, ensuring smooth and intuitive decision-making throughout the gameplay.
User who haven't used a console before might as well be more familiar with this option, since it's not necessary to enter a lot of text or choose numbers from different options.

### story telling experience
To elevate the user experience, the text is deliberately revealed gradually on the screen, simulating the sensation of being written in real-time. This creates an intresting effect, akin to unfolding the pages of an actual story. This is allowing users to engage more deeply with the narrative as if reading a captivating tale, one sentence at a time. This approach aims to enhance the overall storytelling ambiance for a better user experience.

## Features

### Existing Features

#### start screen
The game commences with a start screen, featuring ASCII art, the title, and a count of the discovered endings. This screen serves as an introduction, providing a brief overview of the game's premise. Users are presented with options to initiate the game, reset their progress, or exit the application.

![start screen](/assets/img/readme/ascii-art.png)

![start screen](/assets/img/readme/start.png)

#### Deleting the current score
To reset all endings the user can delete the current scores by choosing this option from the main menu.
Feedback about the progress is shown to the user and confirmation is needed before deleting.

![delete option](/assets/img/readme/delete-yes.png)

![delete](/assets/img/readme/delete-no.png)

#### End the Game
To end the game savely this option is offered in the start screen as well as after finishing the run.

#### Entering a name
Upon initiation, the game prompts the user to provide their name and validates the input received. Following this, the user is greeted by name, establishing a personalized connection. While the name isn't presently integrated into the gameplay, it is intended to utilize the player's name in conjunction with the discovered endings to formulate a leaderboard.

![name](/assets/img/readme/name.png)

#### Story, Chosing an answer
At the core of the game lies the text-based storytelling. The interactive nature of the game unfolds through the selection of options that shape the story's progression. The user is prompted for feedback, and a set of options is presented, inviting the player to actively participate and make decisions that influence the direction of the narrative. This dynamic interaction not only engages the player in the unfolding tale but also empowers them to be a key architect of the story and explore different options.
The whole story is written by myself.

![game](/assets/img/readme/game.png)

#### Finding an ending
When an ending is found the user is presented with "the end" in ascii art as well as the number and name of the ending.

![end](/assets/img/readme/end.png)

#### SpreadSheet
The google sheet works as a database, designed to store the endings found by the user.
Each ending gets written into the google sheet when found and reset to the default value when deleted.

![Google Sheet](/assets/img/readme/sheet.png)

### Possible Future Features

#### Accessibility
* It would be great to support text-to-speech functionality, so that players with visual impairments can enjoy the game.
* It would be cool to customizable text size and contrast options, so that players with different visual preferences can comfortably play the game.

#### Easier Replay
* As a player that returns to the story multiple time, the slow text can be annoying. I would love to have a fast-forward option for previously read text, so that the player can explore alternative paths without re-reading entire sections, or getting them faster.
* To find specific endings it would be great to save mid decision, so the player can explore paths later. 

#### Multiple Accounts
* Currently the game is build with one sheet that saves all the progress for everyone playing this game. It would be great to implement a login, so each player has there own save.
* The inclusion of a highscore board adds a competitive and goal-oriented dimension to the gaming experience. Players can compare their achievements, such as the number of endings discovered or other relevant metrics, fostering a sense of accomplishment and encouraging replayability.

## Testing

### Validator Testing

#### Lighthouse
The site pass the lighthouse test without Problems.
Only SEO could be better.

 ![lighthouse test result](/assets/img/readme/lh-test.png)

#### PEP8
All python code has been validated with the [pep8ci](https://pep8ci.herokuapp.com/) CI Python Linter.
There are no errors.

![run.py](/assets/img/readme/run.png)
![player.py](/assets/img/readme/player.png)
![levels.py](/assets/img/readme/levels.png)

### Manual Testing

#### Name Input

| Feature                                   | Expected Outcome                                                                                                                                                           | Testing Performed                                       | Result                                                             | Pass/Fail |
|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|--------------------------------------------------------------------|-----------|
| Name needs to start with a capital Letter | If the user enters a name that doesn't start with a capital letter, an error message shows up, the rules for a name are repeated and the user can enter a new name choice. | name "okay" is entered                                  | Error message shows up, rules show again, new input can be entered | Pass      |
| Name only includes letters                | If the user enters a name that contains non letters, an error message shows up, the rules for a name are repeated and the user can enter a new name choice.                | name "Test123!" is entered                              | Error message shows up, rules show again, new input can be entered | Pass      |
| Name can't be longer than 10 characters.  | If the user enters a name that is longer than 10 characters, an error message shows up, the rules for a name are repeated and the user can enter a new name choice.        | name "HallodiesisteinTestObdashierzulangist" is entered | Error message shows up, rules show again, new input can be entered | Pass      |
| Valid Names should be accepted            | If the user enters a valid name, the game should start.                                                                                                                    | name "Ella" is entered.                                 | Game starts                                                        | Pass      |


#### Level Design
To test the level design, each potential ending undergoes a examination to ensure it can be reached through the intended pathway. This involves manual testing, where every conceivable route leading to an ending is carefully evaluated and documented in the corresponding test files. The path is represented by the sequence of options chosen during gameplay, with each number denoting the position of the respective answers. For instance, "4 - 2 - 1" signifies selecting the 4th option, followed by the 2nd, and finally the 1st option in the given context. This protocol ensures a comprehensive validation of the game's various storylines and endings.
Due to the size of the file, the results can be found in a seperate file called "level-testen", which is saved in [CSV](/assets/tests/level-tests.csv) and [PDF](/assets/tests/level-tests.pdf) Version.

#### Delete Score
| Feature                                                                        | Expected Outcome                                                                                                                       | Testing Performed                   | Result                                                                                     | Pass/Fail |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|--------------------------------------------------------------------------------------------|-----------|
| When a user selects to delete the score, they should be asked if they are sure | A text asks the user to validate the choice to delete the score                                                                        | Pressing "delete the current score" | The Text "Are you sure .." asks the user for validation                                    | pass      |
| If pressed "no" the score should not be deleted.                               | when the user enters "no" when asks about the deletion for the score, the score should not be deleted and the user should be informed. | writing no                          | "Your score has not been deleted." shows up on the scrren and the score is not deleted.    | pass      |
| if pressed "yes" the score should be deleted.                                  | When the user enters "yes, the score should be deleted and user be informed about the progress.                                        | writing yes                         | "Your score is getting deleted" and "Your score is deleted" appears. the score is deleted. |           |

#### Exit Game

| Feature                                                 | Expected Outcome                             | Testing Performed       | Result                               | Pass/Fail |
|---------------------------------------------------------|----------------------------------------------|-------------------------|--------------------------------------|-----------|
| When "End the game" is entered the program should exit. | The game exits and the python program stops. | Choosing "End the game" | The game ends and the program closes | pass      |


#### Restart or Exit Game after ending is found

| Feature                                                     | Expected Outcome                             | Testing Performed           | Result                               | Pass/Fail |
|-------------------------------------------------------------|----------------------------------------------|-----------------------------|--------------------------------------|-----------|
| When "Enough for today" is entered the program should exit. | The game exits and the python program stops. | Choosing "Enough for today" | The game ends and the program closes | pass      |
| When "restart the game" is chosen the game should restart   | Game restarts                                | Choose "Restart the game"   | The game restarts                    | pass      |


### Unfixed Bugs

#### User iput while slow text
While the text is slowly printed on the screen, every input made by the user is displayed in the text.
One potential solution is to temporarily disable keyboard input during the slow printing process. By implementing this approach, you ensure that user inputs are not inadvertently displayed in the text until the printing is complete. 

![bug-text](/assets/img/readme/bug-text.png)

### Fixed Bugs



##### "Inventory takes 1 argument, but 2 were given"
![bug inventory](/assets/img/readme/bug-inventory.png)
After implementing the is_in_inventory it looked like this:

```
    # --- Check inventory --- #
    def is_in_inventory(obj):
        """
        Returns true if given object is in the players inventory.
        Returns false if given objects is NOT in the players inventory.
        """
        if obj in self.inventory:
            return True
        else:
            return False
```
Taking only on argument, the obj to check for, into account.
But since multiple instances of a player object can be build, the code needs to be given a self to check.

Solution:

```
    # --- Check inventory --- #
    def is_in_inventory(self, obj):
        """
        Returns true if given object is in the players inventory.
        Returns false if given objects is NOT in the players inventory.
        """
        if obj in self.inventory:
            return True
        else:
            return False
```


##### "level12() missing 1 requirement positional argument: 'player'""

![bug player missing](/assets/img/readme/bug-player-missing.png)

To transfer the current player object that contains the stats of the player from level to level it need to be handed down from function to function.

Here I have missed to call the function level12() with the player object:

```
level12()
```

By giving it the current player, it can get and update stats inside the player object.

```
level12(player)
```

## Dependencies
To start the python program succesfully, the following Dependencies are needed:
* google-auth==2.22.0
* google-auth-oauthlib==1.0.0
* gspread==5.10.0
* questionary==2.0.1

## Deployment

### Local Development

#### How to Clone

1. Click the code button and copy the link of your preferred clone option.
2. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
3. Type 'git clone' into the terminal, paste the link you copied in step 1 and press enter.

To run the program directly in your terminal, you have to navigate into the folder you just cloned and runt the comman:

```
python3 run.py
```

Make sure to have python installed.


#### How to Fork

To fork the repository:

1. Log in (or sign up) to Github.
2. Go to the repository for this project.
3. Click the Fork button in the top right corner.
4. Under "Owner," select the dropdown menu and click an owner for the forked repository.
5. By default, forks are named the same as their upstream repositories. Optionally, to further distinguish your fork, in the "Repository name" field, type a name.
6. Optionally, in the "Description" field, type a description of your fork.
7. Optionally, select Copy the DEFAULT branch only.
8. For many forking scenarios, such as contributing to open-source projects, you only need to copy the default branch. If you do not select this option, all branches will be copied into the new fork.
9. Click Create fork.

### Deployment using Heroku

1. Register for an account on Heroku or sign in.
2. Create a new app.
3. Name your App.
4. Add Node JS and Python packages to app setting.
5. Connect github repository to Heroku app
6. Deploy from "deploy", or choose an automatic deploy option.


## Credits
* Markdown Table of Content by [Jon Schlinkert](https://github.com/jonschlinkert/markdown-toc)
* All Ascii Art is from [asciiart.eu](https://www.asciiart.eu/nature/sunset)
* The Libary questionary and there docs can be found [here](https://questionary.readthedocs.io/en/stable/)
* After some trouble with displaying the slow text, this [youtube video](https://www.youtube.com/watch?v=m1oOFS8X-4s) was used.
* I used [AutoPEP8](https://packagecontrol.io/packages/AutoPEP8) as a Formatter in Sublime Text
* The background CSS Art is from [css-pattern.com](https://css-pattern.com/)
* To make pretty markdown tables, [tablesgenerator.com](https://www.tablesgenerator.com/markdown_tables#) was used.