## **Backend Home Assessment**

***
![Doctor](https://www.mytradebee.com/wp-content/uploads/2022/08/78892-doctor-profile.gif)

### **Introduction**
The necktie doctor list is developed with Django, a free and open-source, Python-based web framework. To fetch the doctor list and individual details and register a new doctor Django REST framework is used to build Web APIs.

***

### **Prerequisites**
***
+ Python

  - Make sure to have Python installed & running on your computer. You can skip this step if you already have installed Python on your computer. Please use Python version 3.

  - For Windows
    - Download python from https://www.python.org/downloads/
    - Select Python version 3.9 to download.
    - Download and install.

  - For Linux
```
sudo apt update
sudo apt install python3
```

+ Check the Pip version
```
py -m pip --version
upgrade pip
py -m pip install --upgrade pip
```

+ Virtualenv
  - Make sure to have the **virtualenv** installed globally & running on your computer. If you already have installed on your computer, you can skip this step.
  - Virtualenv installation command for Linux & mac os
```
python3 -m pip install --user virtualenv
```
  - Virtualenv installation command for Windows
```
py -m pip install --user virtualenv
```

***

### **Installation**
***

Make sure to have all the above prerequisites installed & running on your computer.

After you finish with the above steps, you can run the following commands into the terminal/command prompt from the root directory of the project to run the project locally or build for production use:

| Command | Description |
| ------ | ----------- |
| python -m venv environment_name | Create Virtual Environment on Linux & mac OS. |
| python -m venv environment_name | Create Virtual Environment on Windows OS. |
| source environment_name/bin/activate | Activate Environment on Linux & mac OS. |
| environment_name/Scripts/activate | Activate Environment on Windows OS. |
| pip install -r requirements.txt | The following command will install the packages according to the configuration file requirements.txt. |

**Note:** Depending on your installation, you may need to use either pip3 or pip, and for python, you may need to use either python3 or python.

***

##### **Create .env file**
Create a .env file in the same directory where settings&#46;py resides. We will be using [python-decouple 3.6](https://pypi.org/project/python-decouple/) it store parameters in ini or .env files. This package is listed in the requirements.txt.

***

##### **Updating settings&#46;py and importing parameters from .env**

We will update the following:
+ SECRET_KEY
+ DEBUG
+ ALLOWED_HOSTS
+ DATABASES

First, we have to import the config from decouple. In this project, you will find the below line at the beginning of the settings&#46;py file 
```
from decouple import config
```

***

Next, update SECRET_KEY, DEBUG, and ALLOWED_HOSTS.
```
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(',')
```

***

If you're using SQLite Database (Default)
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
==If you're using SQLite as your database, you have to create a file name db.sqlite3 in the project root directory.==

***

If you're using MySQL Database
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.#databaseservername#',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
        'OPTIONS': {  
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
        } 
    }
}
```
==This project is tested on MySQL database and requirements.txt contains mysqlclient version 2.1.1. For the Postgres database need some changes might be needed.==

**Note:** visit this URL for more information about how to configure Django databases https://docs.djangoproject.com/en/4.0/ref/databases/ 

***

##### **Configure .env file**
The below configuration is if you're using SQLite Database.
```
ALLOWED_HOSTS="127.0.0.1,localhost"
DEBUG="True"
SECRET_KEY="your_django_secrect_key"
```

The below configuration is if you're using MySQL or Postgres Database.
```
ALLOWED_HOSTS="127.0.0.1,localhost"
DB_HOST="Write down host"
DB_NAME="Your Database Name"
DB_PASSWORD="Database User Name"
DB_PORT="Write down port"
DB_USER="Your Password"
DEBUG="True"
SECRET_KEY="your_django_secrect_key"
```
**Note:** visit this website to generate the secret key https://djecrety.ir/


***

##### **Run the below command for database migration**
```
python manage.py migrate
```

***

##### **To create a superuser run the below command**
```
python manage.py createsuperuser
```
+ enter username Your Username
+ enter your Email Address
+ enter your Password
+ enter your Password again

***
##### **Django admin panel**

Visit the below link to log in to the admin panel.
```
https://<domain>/admin
```
**Note:** Before registering a doctor, please ensure that you have added category, district, and gender. You can add these data from the Django admin panel.


***

##### **Run the below command to run project**
```
python manage.py runserver
```

***

##### **Run the below command to project testing**
```
python manage.py test necktie_doctor
```

***

##### **Site URL**
+ Doctor list
```
https://<domain>/doctor
```

+ Filter doctor list
  - Query Parameters
    - page_size
    - max_price
    - min_price
    - district
    - category
    - language

```
https://<domain>/doctor/?max_price=amount
```

+ Doctor details
```
https://<domain>/doctor/id
```

***

##### **Register a Doctor**
You can find dummy data in the txt file named single_doctor_reg.txt. Visit the below link to register a doctor. 
```
https://<domain>/doctor/register
```
**Note:** Before registering a doctor, please ensure that you have added category, district, and gender. You can add these data from the Django admin panel.

***


### **Questions and Answers**

***

##### **Choice of Framework & Library:** Please explain why you choose the particular framework or library.

a. What are the benefits & drawbacks associated with that choice?

The task required to finish with Python 3.6+. Python is often used to develop the back end of a website or application. There are a couple of choices for Python-based web frameworks. But among them, Django and Flask are the most popular. Django is best suited for developing large and complex web applications, while Flask is a lightweight, extensible framework that allows you to create small web applications.

First of all, I will discuss the benefits associated with my choice. I choose to use Django as its documentation is well explained, and the support forum is active, continuous update, secure and enterprise-level. Django is ORM based and has a templating engine that helps a developer build a web application very fast. 

It is also highly maintainable. We can also develop microservices. It can work with any client-side framework and deliver content in almost any format (including HTML, RSS feeds, JSON, and XML). Also, Django can run on any Operating System (Windows, Linux, and mac) as it is based on python. 

Django REST framework (DRF) is a powerful and flexible toolkit for building Web APIs. It has both ORM and non-ORM serializer support. Support both function-based and class-based views. Also, have an authentication method for Django. DRF serializers come with both manual serialization and model serialization. It is highly customizable. Pagination, request throttling, testing, and many more features are pre-built in this toolkit. 

They are a popular web framework; many hosting providers give dedicated support. The digital ocean has images for Django. Also, cPanel included a python application section in their system where a simple configuration can run Django. If someone wants to deploy Django in docker and scale the application, it's very handy to use CapRover. CapRover uses docker under the hood. 

Now let us discuss the drawbacks. For a web application, speed is always a major concern. Python is often criticized for its speed. And Django is based on python. It is an interpreted script language, making it relatively slower than many of its compiled counterparts, such as C/C++  or Java. Therefore GO and Spring boot is another backend framework popular for their speed. Multiprocessing is an important part of writing an application, but Python doesn't support it. 

In addition, the number of Django developers is less than Nodejs, Laravel, and React. The person with intermediate knowledge and who loves python mostly learn python based web application.   

In conclusion, Python is a powerful language, and Django is based on it. There is no question about the security and quality of the Django framework. Many giant companies used this framework. 
 
****

b. What are the assumptions underlying that choice?

For an online insurance company, there was no doubt that the web application would be on a large scale. Also, the application should be developed on a reliable framework. Django is a perfect fit for it. The points I took into consideration are:

+ Should be Python-based. 
+ The application should be scalable. 
+ Security is always a big priority for any application, and Django provides that.
+ Framework that has dedicated support for SQL databases but also can work with non-SQL. 
+ API is fully documented and supported by a vast community.
+ Support microservice and maintainable code. 

***

##### **Potential Improvement:*** Please elaborate on what kind of improvements you would like to implement if you have given more time.

The improvements I would like to implement to doctor list API if given more time are listed below:

+ Add doctor gallery. Showing his profile with his practicing pictures.
+ API link to update doctor details.
+ API link to delete doctor details.
+ API link for the related doctor randomly. 
+ Advance filtering like a nearby doctor by radius, doctor available on public holidays and weekends, a doctor by gender, and working hours.
+ If the API is used for web frontend clients, then the doctor id and name as a slug in the URL should be more appropriate for SEO. 

Additional features that can be implemented in the long run:
+ Add clinic or hospital option, same as a doctor. 
+ Featured doctor or clinic. Doctors or hospitals can pay to list them at the top for a certain time. 
+ User portal showing their plan and past medical record.
+ User subscription and online payment method. 
+ Mobile application API development. 
+ API throttling limits the number of requests so that no one can abuse them.


I believe this will give an idea of my vision for this project.
 
***

##### **Production consideration:** Any extra steps should be taken with caution when deploying your app to a production environment?

+ It is highly recommended to use Debug = False in production. Please change the Debug in the .env file. 
+ Install everything in requirement.txt 

***

##### **Assumptions** 
a. Any assumptions you made when you designed the data model and API
schema?

+ For the doctor model, I went through some websites to get an idea. I then designed the model accordingly. 
+ For the API list, I tried to follow the UI design provided. 
+ For API URL format and API data filtering, I did it according to the assessment file. 

b. Any other assumptions and opinions you have taken throughout the assessments?

No 










