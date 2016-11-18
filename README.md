# Connect Four game
This is a timed python test for Deviget.
The idea is to implement the classic game Connect Four. (http://en.wikipedia.org/wiki/Connect_Four)

## Architecture
The game was implemented with Django 1.10
Two custom Apps were created for this site:

### board
In this app we have the main functionalities and models of the site.
The models.py file contain the data modeling of the game and some functionality to play the actual game (I suggest to read the inline doc of this file to understand better how the data is stored).
In the tests.py file we have tests that checks and demostrate the usage of the models.
views.py file has the views that use the models actions to perform the game play.

### common
This app contains some helpers that can be used across the site, like common templatetags, sipmle views and pages.


## With the given time we covered:

 * Project setup and configuration.
 * Data model design.
 * Basic game logic and how it's connected with the data modeling.
 * Unit test for key functionalities of the site
 * Simple Views and UI to test and use the existing functionality.

## Next steps

 * Finish game logic such us winner detection and turns to play
 * API implementation (Django Rest Framework)
 * Game authentication and secuirity
 * Better UI, with the usage or a front-end framework
 * More unit test and functional tests.
 * Other good practices can be added like automatic deployments, continous integration, etc.

## Tests

  * running tests: `./manage.py test`


## Deployment

You can visit and test the web app on:

http://rafen.webfactional.com/

It's deployed on hosting of Webfaction.
Admin UI: http://rafen.webfactional.com/admin/


## Usage:

Home Page
![Home Page](https://dl.dropboxusercontent.com/u/14133267/static/ConnectFour.png)

Board Page
![Board](https://dl.dropboxusercontent.com/u/14133267/static/ConnectFourBoard.png)

Admin Site
![Admin](https://dl.dropboxusercontent.com/u/14133267/static/ConnectFourAdmin.png)

