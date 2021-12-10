Hello, here is a readme for this project

First of all, the dependencies you will need are:
- Python3
  - Django==3.2.6
  - django-ckeditor==6.2.0
  - django-cleanup==5.2.0
  - django-js-asset==1.2.2
  - Pillow==7.0.0
  - whitenoise==5.3.0
  
You can install this by installing python3 at python.org
Then go into a terminal and type a couple of lines:
  - pip install django
  - pip install django-ckeditor
  - pip install django-cleanup
  - pip install django-js-asset
  - pip install Pillow
  - pip install whitenoise
  
Now you should be able to run it.

For people who never used django here is an explenation on how to run it:
Go into a terminal and navigate to the main folder (there should be a manage.py)
When there type 'python manage.py runserver'
now you are hosting a personal server at 127.0.0.1:8000 by default.
To view this website add /main/home/ at the end.

There is also a admin site that you can not see.
View this by typing python manage.py createsuperuser and create a account.
Then run the server again and add /admin/ to the main url and login.
