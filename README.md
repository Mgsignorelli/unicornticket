# Support Ticket System - Django Frameworks Project

[![Build Status](https://travis-ci.org/Mgsignorelli/unicornticket.svg?branch=master)](https://travis-ci.org/Mgsignorelli/unicornticket)

This is the Django Fullstack Frameworks Unit Milestone Project, for Code Institute's Full Stack Web Developer Course.

## UX
The following wireframe was designed to represent the website skeletal framework.

![Wireframe](public/images/mock.png "Wireframe") 

Prior to the web application creation, a Relational Database was mapped with the PonyORM tools (https://editor.ponyorm.com). The resulting diagram below represents the different tables and relationships between them.

![PonyORM relational database map](public/images/ponydiagram.png "Database Map")

## Features

### Existing Features

## Technologies Used

- HTML language, to write the web page layout. 

- CSS and Sass language to style the application.

- Yarn, JavaScript package manager (https://yarnpkg.com/lang/en/).

- Font Awesome (https://fontawesome.com/)
    Font and Icon toolkit

- Font Google (https://fonts.google.com/)
    Font toolkit.

- Bootstrap 4 (https://getbootstrap.com/docs/4.0/getting-started/introduction/)
    Framework used to uniform the layout. Also, the spacing utils section has been creaated from the information in https://getbootstrap.com/docs/4.1/utilities/spacing/.
    
- Media Queries were used to control the responsive adjustments for smallest screens of the subtitles and paragraphs.

- Slate Bootstwatch was used as a Theme (https://bootswatch.com/3/slate).

- Python, backend language, to create the server of the game application.

- PonyORM, Python Object-Relational Mapper.  

- Heroku, for deployment.
    
- Sqlite3 database engine (https://www.sqlite.org/index.html). This was used for development.

- Postgres (https://www.postgresql.org), database engine used for the deployed version on Heroku.

- TravisCI (https://travis-ci.org/), for automated testing prior to development.

- GitKraken (https://support.gitkraken.com/), for management of Branch and Git commits.

- WTF Form Validators (http://wtforms.simplecodes.com/docs/0.6/validators.html), verifying the form input fulfills some criterion.

- Sentry (https://sentry.io/welcome/), platform for monitoring exceptions.

- Select2, (https://select2.org/), jQuery replacement for select boxes.

- Python PEP8 checker (http://pep8online.com/)

## Development

### Requirements
- [Python 3.4.9](https://www.python.org/downloads/release/python-349/) is required.

### Preparation
- Clone repository
- Copy `env.example` to `env.py` and enter values for all environmental variables listed.
- Run `pip install -r requirements.txt` (or `pip3` if necessary for Python 3).
- Run any migrations using:
  - `python manage.py makemigrations` (or `python3` if necessary)
  - `python manage.py migrate`
- Run `python manage.py collectstatic` to generate static files.
- Run `python manage.py runserver` and browse to generated local URL.

## Testing

Testing was performed through automated and manual tests. 

Python code is PEP8 compliant, checked through http://pep8online.com/

Travis CI integration was configured to perform automatic tests -using testunit.py- before deployment.

This application was extensively tested in different browsers, 
screen sizes and Operative Systems, since it was originally designed in a Mac Desktop.

Manual Browser testing was performed through acting like a user in the web page, 
utilizing all the features.

An example of a manual browser test was User creation.

A. User Creation:
  1. In home, go to Register
  2. Submit a user name, longer than three characters
  3. Submit an email address, must be valid
  4. Submit a password and confirm it
  5. See a welcome message in the Navbar
  6. Be allowed to vote a recipe
  7. Logout with link in Navbar
  
## Deployment

This project was deployed through Heroku, it can be found here:
https://issuetrackersystem.herokuapp.com/

Heroku allows automatic deployment from a chosen branch.
Travis CI integration was configured to perform automatic tests before every deployment.

In this case, the deployed branch is the master branch. 

Development was done in the development branch managed through GitKraken.

Postgresql Database is used in the deployed version instead of SQLite, which was used for development. SQLite is not 
suitable for Heroku because Heroku deploys a managed container system and will therefore erase any added or edited 
information in the live version with each deployment.


Use the following credentials in order to test Admin function:


For environment variables in development .env was used. For deployment, the variables were manually set.

### Requirements
Python 3.4.9 is required. 

### Preparation
Clone repository
Copy env.example to env.py and enter values for all environmental variables listed.

Run pip install -r requirements.txt (or pip3 if necessary for Python 3).

Run any migrations using:
python manage.py makemigrations (or python3 if necessary)
python manage.py migrate
Run python manage.py collectstatic to generate static files.
Run python manage.py runserver and browse to generated local URL.

## Credits

### Media
