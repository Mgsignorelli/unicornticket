# Support Ticket System - Django Frameworks Project

[![Build Status](https://travis-ci.org/Mgsignorelli/unicornticket.svg?branch=master)](https://travis-ci.org/Mgsignorelli/unicornticket)

This is the Django Fullstack Frameworks Unit Milestone Project, for Code Institute's Full Stack Web Developer Course.

## UX
The following wireframe was designed to represent the required website skeleton.

![Wireframe](static/img/uniMock1.png "Wireframe") 

## Features
This Ticket System is the Unicorn Attractor App Helpdesk.
 
The Unicorn Attractor App allows the user to emit our Super Secret Unicorn Frequency from their mobile device and attract 
all the Unicorns. 
The App is linked at the top right corner of the screen, in the Navbar. 

_______

The objective of the Helpdesk is to allow the users of the Unicorn Attractor App to report Bugs and to request Features 
they would like to have in the Unicorn Attractor App. 

A logged in user can create a ticket as either a feature or a bug, comment on a ticket and buy votes from the vote shop.
The user will need to have purchased votes to vote for a feature. Bugs can be upvoted free of charge. 
An admin has all the actions of a user, plus the ability to edit and delete Tickets and Comments.

An index with all existing Features and another one with all existing Bugs are visible for every user, logged in or not.
These are linked from the Navbar at the top of the website. The Navbar has further links to Ticket Creation, Buy Votes,
the Unicorn Attractor App, the user's profile and the capability of login and logout. 

The Unicorn Attractor App developer will spend half of their time working on the highest voted Feature.
The breakdown of this work is displayed in the index through charts. 

Comments have the user's name, but Bugs and Features can be requested and reported anonymously.
Votes can be bought from the Helpdesk in the Buy Votes section, linked permanently in the Navbar. 
The user is redirected to the Stripe checkout system to ensure secure card payments. 
A user can see their order history in their profile, linked as well in the Navbar.

In the Helpdesk home, a user can immediately see buttons that will take them to either Create a Ticket or to Buy Feature Votes.
Below, the user finds graphics displaying the amount of worked on features for each day, week, month and year (last twelve months).
The most voted Feature and Bug are also displayed.


Use the following credentials for the Admin User:
Username: admin
Password: 1234qwer


## Technologies Used

- HTML language, to write the web page layout. 

- CSS to style the application.

- Font Awesome (https://fontawesome.com/)
    Font and Icon toolkit

- Font Google (https://fonts.google.com/)
    Font toolkit.

- Bootstrap 4 (https://getbootstrap.com/docs/4.0/getting-started/introduction/)
    Framework used to uniform the layout. Also, the spacing utils section has been creaated from the information in https://getbootstrap.com/docs/4.1/utilities/spacing/.
    
- Lux Bootstwatch was used as a Theme (https://bootswatch.com/3/lux).

- Django (1.11) (https://www.djangoproject.com/), to create the backend application.

- ChartJs (https://www.chartjs.org), to display graphics showing worked on Features and Bugs.

- Heroku (https://www.heroku.com/), for production deployment.
    
- Sqlite3 database engine (https://www.sqlite.org/index.html). This was used for development.

- Postgres (https://www.postgresql.org), database engine used for the deployed version on Heroku.

- TravisCI (https://travis-ci.org/), for automated testing prior to development.

- Behave (https://behave.readthedocs.io/en/latest/), for Behaviour Driven Development.

- Selenium (https://selenium-python.readthedocs.io/api.html), for Web UI Automation Testing.

- Splinter (https://splinter.readthedocs.io/en/latest/), for testing through user Browser Action Automation.

- Stripe (https://stripe.com/gb), for secure card payments.

- GitKraken (https://support.gitkraken.com/), for management of Branch and Git commits.

- Python PEP8 checker (http://pep8online.com/)

- AWS - S3 storage bucket (https://aws.amazon.com/), to serve static files.

- Boto3 to connect the S3 storage bucket to Django.

### Requirements
- [Python 3.4.9](https://www.python.org/downloads/release/python-349/) is required.

### Preparation
- Clone repository
- Copy `.env.example` to `.env` and enter values for all environmental variables listed.
- Run `pip install -r requirements.txt` (or `pip3` if necessary for Python 3).
- Run any migrations using:
  - `python3 manage.py makemigrations`
  - `python3 manage.py migrate`
- Run `python3 manage.py collectstatic` to generate static files.
- Run `python3 manage.py runserver` and browse to generated local URL.

## Testing

Testing was performed through automated and manual tests. 

Python code is PEP8 compliant, checked through http://pep8online.com/

Travis CI integration was configured to perform automatic tests before deployment.

This application was extensively tested in different browsers, 
screen sizes and Operative Systems, since it was originally designed in an iMac.


An example of a manual browser test was User creation.

A. User Creation:
  1. In home, go to Register
  2. Submit a user name
  3. Submit an email address, must be valid
  4. Submit a password and confirm it
  5. See a welcome message beneath the Navbar
  6. Be allowed to upvote a Bug
  7. Be allowed to Buy Feature Votes
  8. Be allowed to vote on a Feature
  9. Logout with link in Navbar
  
## Deployment

This project was deployed through Heroku, it can be found here:
https://issuetrackersystem.herokuapp.com/

Heroku allows automatic deployment from a chosen branch.
Travis CI integration was configured to perform automatic tests before every deployment.

In this case, the deployed branch is the master branch. 

Development was done in the Development branch managed through GitKraken.
A separate Feature branch was used to develop each of the individual features.

Postgresql Database is used in the deployed version instead of SQLite, which was used for development. SQLite is not 
suitable for Heroku, since Heroku deploys a managed container system and will therefore erase any added or edited 
information in the live version with each deployment.

For environment variables in development .env was used. For deployment, the variables were manually set.


Use the following credentials in order to test Admin function:
Username: admin
Password: 1234qwer

### Requirements
Python 3.4.9 is required. 


### Media
Image in Unicorn Attractor App adapted by me, from a royalty free image.
