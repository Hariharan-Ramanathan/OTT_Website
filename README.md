# OTT

OTT is an online platform clone for releasing and watching new movies. As of now instead of videos, Images alone were uploaded.

# Installation
    1) Install Python 3.8
        Linux   : $ sudo apt install python3.8
        Windows :- Download Python 3.8 from the website given below and after installing it add its path to environment variable
                    https://www.python.org/downloads/windows/
        MaxOs   : https://www.python.org/downloads/mac-osx/
        
    2) Install Pip
        Linux   : $ sudo apt install python3-pip
        Windows : - Download get-pip.py to a folder on your computer.
                  - Open a command prompt and navigate to the folder containing the get-pip.py installer.
                  - Run the following command.
                        $ python get-pip.py
                  - Add pip path to environment variable
        Mac     : - curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
                  - $ python3 get-pip.py
    3) Install Django
            $ pip install django==2.2 
    4) Download the Github Project
            $ git clone https://github.com/Hariharan-Ramanathan/OTT_Website.git
    5) Enter into project Folder and create a Virtual Environment 
            $ python3 -m pip install pipenv --upgrade
                        or
            $ python -m pip install pipenv --upgrade
    6) Install python 3.8 and django in Virtual environment
            $ pipenv install --python 3.6 django==2.2
    7) Enter into Virtual Environment
            $ pipenv shell
    8) Install django-filter inside virtual environment
            $ pip install django_filter 

# Run server
    1) Enter into Virtual Enviromnent
            $ pipenv shell
    2)      $ ./manage.py runserver 
                    or
            $ python3 manage.py runserver
            
# Create Admin 
     1) Enter into Virtual Enviromnent
            $ pipenv shell
     2)     $ ./manage.py createsuperuser
                     or
            $ python3 manage.py createsuperuser

# Admin Credentials
    - Admin 
        Username : harish
        Password : Malli1970

# User and Admin        
- User
    1) Can view website, 
    2) Can rate a movie(only once),
    3) Can sort and filter according to their choice
- Admin
    1) Can Upload new Movie,
    2) Can delete an uploaded Movie,
    3) Can view website, 
    4) Can rate a movie(only once),
    5) Can sort and filter according to their choice
    
    
  
