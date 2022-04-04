# The Pantry

## Introduction


![Screenshot of homepage](./assets/screenshots/main-menu-zoomed-in.png)

[View the live website on Heroku](https://pp4-the-pantry.herokuapp.com/)
Please note: To open any links in this document in a new browser tab, please press CTRL + Click.

## Table of Contents
* [User Experience Design (UX)](#UX)
    * [The Strategy Plane](#The-Strategy-Plane)
        * [Site Goals](#Site-Goals)
        * [Epics](#Epics)
        * [User Stories](#User-Stories)
    * [The Scope Plane](#The-Scope-Plane)
    * [The Structure Plane](#The-Structure-Plane)
        * [Opportunities](#Opportunities)
    * [The Skeleton Plane](#The-Skeleton-Plane)
        * [Wireframes](#Wireframe-mockups)
        * [Logic Flow](#Logic-flow)
    * [The Surface Plane](#The-Surface-Plane)
* [Features](#features)
* [Future Enhancements](#future-enhancements)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## UX
### The Strategy Plane

*  

#### Site Goals

* 
* 
* 

#### Epics

10 Epics were created which were then further developed into 38 User Stories. The details on each epic, along with the user stories linked to each one can be found in the project kanban board [here](https://github.com/MattBCoding/pp4-the-pantry/projects/1)

1. Initial Django setup [#1](https://github.com/MattBCoding/pp4-the-pantry/issues/1)
2. User Profile [#2](https://github.com/MattBCoding/pp4-the-pantry/issues/2)
3. User sign in or sign out [[#3](https://github.com/MattBCoding/pp4-the-pantry/issues/3)]
4. User recipes [#4](https://github.com/MattBCoding/pp4-the-pantry/issues/4)]
5. Recipe management [#5](https://github.com/MattBCoding/pp4-the-pantry/issues/5)] 
6. Recipe searching [#6](https://github.com/MattBCoding/pp4-the-pantry/issues/6)
7. recipe viewing [#7](https://github.com/MattBCoding/pp4-the-pantry/issues/7)
8. recipe interaction [#8](https://github.com/MattBCoding/pp4-the-pantry/issues/8)
9. site owner objectives [#9](https://github.com/MattBCoding/pp4-the-pantry/issues/9)
10. recipe rating system [#28](https://github.com/MattBCoding/pp4-the-pantry/issues/28)

### User Stories

From the Epics, 38 User stories were created. Each story was assigned a classification of Must-Have, Should-Have, Could-Have or Won't Have. Each story was also assigned user story points, based on my best estimation for the time/difficulty of completing each story. A combination of being new to story estimation, inexperience with Django and time constraints during development left me completing 61 story points from the initial total of 131. From the initial 131 points, 82 were for Could Have stories. A number of these stories were created based on an ideal scenario of building out the project whilst I knew in the time available it would be unlikely I would complete those stories. I will however revisit them at a later time for a redevelopment of the project.

* 
* 
* 

### The Scope Plane

**Features planned:**
* 
* 
* 
* 


### The Structure Plane

User Story:

> 

Acceptance Criteria:
* 

Implementation:
* 

User Story:

> 

Acceptance Criteria:
* 

Implementation:
* 
*  

User Story:

> 

Acceptance Criteria:
* 

Implementation:
* 

#### Opportunities

Arising from user stories
| Opportunities | Importance | Viability / Feasibility
| ------ | :------: | :------: |
| ** Provide a fun game environment ** | 5 | 5 |
| ** Provide different difficulty levels ** | 5 | 5 |
| ** Provide ability to control the time the game takes ** | 5 | 5 |

### The Skeleton Plane
#### Wireframe mock-ups

Given that the application will be run within a terminal emulator provided within the template, there are limited options available with regards to the layout of the webpage itself. Early on within the development of the theme, I located a suitable background graphic on iStock. To position the terminal appropriately for the background graphic, and keeping user experience in mind, I decided to centre the terminal horizontally on the screen. This positions the terminal window within the lower part of the rail around the ship in the background graphic. The run program button was centrally positioned to above the terminal window to emphasis its importance.

![Home Page Wireframe](/assets/wireframes/homepage-wireframe-900.png)

For the terminal window itself, I also produced a wireframe in the well-known design package Microsoft Excel. Whilst not traditionally used for this purpose, the terminal window dimensions of 80 columns wide by 24 rows high provided a restriction that I could duplicate in excel easily. This enabled me to work out the spacing requirements and dimensions of the elements on screen during the gameplay. Given that all the elements that would be displayed in the terminal are ASCII characters, creating an 80 x 24 grid in excel with one character per tile it enabled me to easily see if I could fit the total information required on each line. This was especially useful whilst calculating how to print the two game boards with a scoreboard in between them, given the line-by-line method in which the terminal prints.

![Terminal Game Play Wireframe](/assets/wireframes/wireframe-game-screen.png)

#### Logic Flow

To develop the logical steps required within the game, along with gaining an understanding of how the different game elements would interact, I created a flow chart detailing the individual steps for the game. Given the scope of the game logic involved the full flow chart resulted in a large image. The full image can be viewed here [Logic Flow Diagram](/assets/logic/logic-flow-full.png)



### The Surface Plane

#### Design

Once I was happy with the overall layout of the page.



## Features
#### Welcome Screen

![Welcome Screen](/assets/screenshots/welcome-screen.png)












## Future Enhancements






## Testing

### Testing Strategy



#### Testing Overview

Testing was divided into different sections to ensure everything was tested individually with test cases developed for each area.

![Testing Schedule Overview](/assets/testing/tes-schedule.png)

A full detailed breakdown of the testing procedures and methodology can be found in the testing.md file [here](TESTING.md)

#### Validator Testing



#### Notable Bugs



#### Libraries Utilised
##### Built in Python Libraries


##### Other Libraries Used

## Deployment

The site was deployed via Heroku, and the live link can be found here - [The Pantry](https://pp4-the-pantry.herokuapp.com/)



### Project Deployment

To deploy the project through Heroku I followed these steps:
* Sign up / Log in to [Heroku](https://www.heroku.com/)
* From the main Heroku Dashboard page select 'New' and then 'Create New App'
* Give the project a name - I entered Calcio-Jack and select a suitable region, then select create app. The name for the app must be unique.
* This will create the app within Heroku and bring you to the deploy tab. From the submenu at the top, navigate to the settings tab.
* This next step is required for creating the app when using the CI Python Deployment Template. If you created your own program without using the CI Template, you might not need to add a config var.
* In the config vars section select the reveal config vars button. This will display the current config vars for the app, there should be nothing already there.
* In the KEY input field input PORT all in capitals, then in the VALUE field input 8000 and select the Add button to the right.
* Next select the add buildpack button below the config vars section.
* In the pop-up window select Python as your first build pack and select save changes.
* Then repeat the steps to add a node.js buildpack.
* The order of the buildpacks is important, in the list Python should be first with Node.js second. If they are not in this order, you can click and drag them to rearrange.
* Next navigate back to the deploy tab using the submenu at the top of the page.
* In the deployment method section select the GitHub - Connect to GitHub button and follow the steps prompted if any to connect your GitHub account
* In the Connect to GitHub section that appears, select the correct account, and enter the name of the repository and select search.
* Once Heroku has located the repo select connect.
* This will connect the repo to the app within Heroku. Below the Apps Connected to Heroku section will be the Automatic Deploys section.
* In this section, confirm the correct branch of the repo is selected in the drop-down box, and then click the Enable Automatic Deploys button
* This will ensure whenever you change something in the repo and push the changes to GitHub, Heroku will rebuild the app. If you prefer to do this manually you can utilise the manual deployment options further down. For this project I utilised the Automatic Deployment to enable me to check changes I made to the app as I developed it.
* Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.

## Credits

### Code




### Content

#### Images

#### Recipes

#### Documentation


### Acknowledgements

I'd like to thank the following:
* Daisy McGirr .
* Sean and Ed at CI Tutor support for their patience and pointing me in the right direction when I went off course.