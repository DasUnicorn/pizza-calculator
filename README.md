# "Work from Home" - Story Telling Game
"Work from home" is an interactive storytelling game where players take on the role of the protagonist in a dynamic narrative. The game can be played in the console or in a virtual console in the web-browser.
The game is centered around your first remote office day, where every choice you make influences the storyline and leads to different outcomes. Try to find as many endings as possible.

Read below to learn how to deploy the game youself or check out the [live-site](https://murmuring-peak-78506-458d466df584.herokuapp.com/).

![Mock up](/assets/img/readme/mockup.png)

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

### Story
In creating the game, my aim was to craft a narrative that commences with a familiar scenario, gradually evolving into an increasingly intricate fantasy realm that rapidly intensifies in complexity and imagination.

### Flowchart
One of the most challenging aspects was maintaining a clear overview of the story and its various plotlines. so it was necessary to create an extensive flowchart to document the progression. Each element within these flowcharts is designated with a star, serving as a marker to indicate the implementation level of the corresponding code (for example objects marked with the star and the number 8 are implemented in the function "level8(player)").
The preview of the board can be seen below. The [full Miro board](https://miro.com/app/board/uXjVNHT1bqI=/?share_link_id=87020844922) can be inspected online.

![Miro Board](/assets/img/readme/miro.png)

### Gameplay
The game operates in the following manner: Users engage by making decisions, and in the background, a player class undergoes updates based on these choices. The player's character can experience growth or decline in stats, contingent on the decisions made. Additionally, the narrative takes divergent paths according to these choices. To achieve particular endings or storylines, players must have specific stats. Each player possesses an inventory where they can collect items, adding an extra layer of depth to the game.

![Player Class])(/assets/img/readme/player.png)

## Features

### Existing Features

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

## Testing



### Validator Testing


#### PEP8


### Manual Testing


### Unfixed Bugs


### Fixed Bugs


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


## Credits
* Markdown Table of Content by [Jon Schlinkert](https://github.com/jonschlinkert/markdown-toc)
* https://patorjk.com/software/taag/#p=display&h=2&f=Big&t=work%20from%20home
* https://www.asciiart.eu/nature/sunset
* https://questionary.readthedocs.io/en/stable/
* https://www.youtube.com/watch?v=m1oOFS8X-4s