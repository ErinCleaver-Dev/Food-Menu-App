* first create a virtual envornment:  python -m venv .venv 
* to activate type in:  .venv/Scripts/activate

* To install django type:  pip install django

*  To update pip: python.exe -m pip install --upgrade pip

* To config the project:  django-admin startproject config ./

* To run the server typ:  python manage.py runserver

* To create a app type: python manage.py startapp app_name

*  Add the new app to the my apps:
   1. go to config
   2. select settings
   3. add to installed apps list.  

* After this def a new view in the views folder 
* It should return a value 
* Then add the url to the config folder.  

*  To create a tablet type in python manage.py migrate
*  To make migrations: python manage.py makemigrations
*  To add to database: python manage.py sqlmigrate name 

To transfer from computer to computer:
 1. First type:   pip freeze > requirements.txt
 2.  Then type:  pip install -r requirements.txt

# https://medium.com/quick-code/deploying-django-app-to-heroku-full-guide-6ff7252578d7