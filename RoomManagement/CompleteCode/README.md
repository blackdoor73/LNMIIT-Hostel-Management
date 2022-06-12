# Room Management module for LNMIIT HOSTEL MANAGEMENT SYSTEM PROJECT
Implemented using python through django framework at backend ,sqlite3 database along with html and css for templates of frontend pages
To Run the django system from the folder 
1)Install python 3 and django on your system

    (Below are Django installation and setup instructions from :https://docs.djangoproject.com/en/4.0/topics/install/ )
    Creating a virtual environment:
        python -m venv project1-env
    Activating virtual environment:
        project1-env\Scripts\activate.bat
    Install Django:
        on windows : py -m pip install Django
        on mac or linux:python -m pip install Django

    Make sure that  Git is installed and that its commands can from a shell. (Enter git help at a shell prompt to test this.)

    Check out (github command)Django’s main development branch using command :
        git clone https://github.com/django/django.git
    Install django from cloned repository
        py -m pip install -e django\
        

2)Clone the CompleteCode folder in repository
3)open terminal on the cloned folder
4)Check django and python installation by running these commands
    To verify python installation use command : py
    To verify django installation use command : 

5) Run these commands for first time implementation
    python manage.py migrate    //for applying migrations locally
    python manage.py creatsuperuser //for creating an admin user account ,fill in username and password 
6)start server using command
    python manage.py runserver      //start the server 
7) Copy the url displayed after previous step in the terminal to the web browser search bar to open the website

