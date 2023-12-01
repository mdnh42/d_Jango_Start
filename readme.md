==================== Django Introduction =========================
### Django ###
# What is Django?
= Django is a web application framework written in python programming language. It is based on MVT (Modal View Template) design pattern. 

It is also called batteries included framework becuase Django provide built-in features for everything. 

# Why Django Framework? 
= Excellent documentation and high Scalability 

# Unique Features of Django
= Admin Interface 
= Object-Relational Mapping (ORM)
= URL Routing 
= Template System 
= Form Handling 
= Security Features 
= Scalability 

# How Does Django Work? 
= User -> Django -> URL -> View -> Modal -> Template 

# MVT 
= Modal (The Data we want to present, usually data from a database)
= View (A request handler that returns the relevant template and content - based on the request from the user.)
= Template (It represent how data should be presented to the application user. It may consist of HTML, css, JS misxed with Django).

====================  Django Environment Setup =====================

# Python Download
[Python Download Link] (https://www.python.org/)
[VS Code DOwnload Link] (https://code.visualstudio.com/)

# Python Install Process 
    - Check must Add python.exe to PATH 

# Python Install Check 
    - open CMD Write: python --version


============== Virtual Environment ================
## What is virtual Environment? 
= A virtual environment is a networked application that allows a user to interact with both the computing environment and the work of other users. Email, chat, and web-based document sharing applications are all examples of virtual environments. 


## How does a virtual Enviroment Work? 
Step # 1: pip install virtualenv
Step # 2: virtualenv --version 
Step # 3: virtualenv my_env
Step # 4: source ./my_env/Scripts/activate
Step # 5: my_env/Script>deactivate 

Step # 6: pip install django
Step # 7: python -m django --version

Step # 8: deactivate (For Specefic)

Step # 9: Install Globally (pip install django)


====== Create Project ========== 
# Add Extension On VS CODE 
    - Python
    - Python Extension pack 
    - Python Indent 
    - Django (BP)
    - Django (Roberth Solil)


# Create Project 
    - django-admin startproject first_project 
    - go to first_project using cd 
    - python manage.py runserver (For VERSER RUN)


# Auto Created File under Your Project (What Purpose)
## Django Project Directy Structure 
    first_project 
        - _pycach_
        - _init__.py 
            (The folder which container __init__.py file is         considered as python pakage)
        - asgi.py 
            (Asynchronous Server Gateway Interface)
        - setting.py 
        (Data Setting- Database, Config Info, Template, Installed Application , Validator etc)
        - urls.py 
        (Contains info of url attached with application)
        - wsgi.py 
        (Synchronous Web server Gateway Interface - WSGI)
        - manage.py 
        (Manage.py is a project-specefic command-line utility)

#  Create Project and Create an Application CMD
    django-admin startproject PROJECT-NAME 
    django-admin startapp APP-NAME 


# Working with urls.py and views.py 
    Create a views.py file under first_project application
    Your Project Project Name First Project 
    and Your Applicatoin Project anem First Project. 

# Set Path: on urls.py 
    from django.contrib import admin
    from django.urls import path
    from . import views 
    urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home)
    ]


# def in ViEWS.js 
    from django.http import HttpResponse

    def home(request):
        return  HttpResponse ("Ths is my first django app")



# Create an APP 
    Project -> 
        Application (url, veiws)-> 
            App (url, views)

    [django-admin startapp first_app] under your project 

# Set setting your project. You created first_app in setting.js's installed app Under First_Project Settings. 

# Set urls.py where first-project. Here write this line path('', include('first_app.urls'))

# Set urls and views 



 ================= Create Project =============== 

 ## Create Project and Set views.py 
    - Create template under main project 
    - Create HTML file under template 
    - set teamplate view
    - Rendering template from application 
    - Template uses html python combined and (Access to write to html and python)

## Django Template Language (IF-ELSE)




## Django Template Language (FOR LOOP)




## Django Template Language (Filtering)

