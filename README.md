# Django-POC

Before following the setup please make sure you have python 3.x installed.

First step is to install the virtualenv
-- sudo pip install virtualenv

Second setp
-- Select a directory or make a new directory where you want to setup your project.

Third step
-- Then, you will need to use “virtualenv” to create a place for the environment-specific dependencies to be installed , command given below
virtualenv /your-directory 
for example I folder python where I want my proj to setup , we do vritualenv/python

Fourth step
-- At this step go to your directery and verify python is installed by using puthon --version. Now activate the virtual env by the below command
source python/myprojectenv/bin/activate.
Your path can differ from what I have above but basically the path should naviagte to a file named activate inside the bin folder which is created in earlier step.

Fifth step
-- Install postgress library required
pip3 install psycopg2 
Before this please sure you have pip3.

Sixth step install django
-- pip3 install django

Seventh Step
Once Django is installed navigate to the bin folder in your termianl and run the below command
django-admin.py startproject "name-of-your project" .  for exmaple django-admin.py startproject pythonpoc .

Now when that step is done you see you will have a bin folder with activate file inside it and also a folder called pythonpoc.
Inside the pythonpoc replace settings.py and also urls.py with the ones this repo.
Also paste the three folders called cars, Person and tutorial inside the bin

Once all these steps are done run the server 
python3 manage.py runserver 0.0.0.0:5000 and naviagate to http://0.0.0.0:5000/

Optional step is to create a superuser who has admin previlages 
To verify that your superuser works, go to the “/admin” page and setupup your user and password
