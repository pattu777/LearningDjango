# LearningDjango
This repo contains code for some of the apps that I built while learning the Django framework. Hosted on a DigitalOcean droplet using Ansible.

### Django Apps
1. Polls

### Technology
```
Back-end - Python 2.7  
Web Framework - Django 1.9  
Database - sqlite3  
Front-end - HTML/CSS/JavaScript  
Front-end tool - Bootstrap  
Operating System - Ubuntu 14.04  
```

### Installation
Clone the repo  

```bash
$ git clone git@github.com:pattu777/LearningDjango.git
```

Change directory  

```bash
$ cd LearningDjango/
```

Create and activate virtualenv(Strongly Recommended)  

```bash
$ virtualenv venv --no-site-packages
$ source venv/bin/activate
```

Install the packages  

```bash
$ pip install -r requirements.txt
```
Go inside the apps folder.

```bash
$ cd apps
```

Run the server  

```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py collectstatic
$ python manage.py runserver
```