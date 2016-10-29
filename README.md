# amplio
This is Amplio, a Django web application, made by me, [Dhruv Bhanushali](http://dhruvkb.github.io), a developer and engineer-physicist at the [Indian Institute of Technology at Roorkee](http://www.iitr.ac.in) in Uttarakhand, India.

I am a prolific member of [Information Management Group](http://img.channeli.in), the computing group of IIT Roorkee credited with maintaining the technological backbone of the institute.

This repository contains my summer assignment that revolved around learning web development with Django.

## Introduction
Amplio is a feedback application for IIT Roorkee. It enables the students of IIT to voice any and all problems or difficulties related to the technical aspects of the institute, so that IMG or other concerned authorities can look into the issue and take suitable action.

## Features
Users may create accounts with minimal profiles and then start posting feedback to the site. Users can also vote their favourite topics to the top so that the concerned parties can quickly see the hot issues and begin solving them. Viewing feedback is open and does not need an account.

Then there's the discussion, where people can add their thoughts to the feedback, improve upon the details, confirm bugs and even suggest workarounds or permanent solutions. Discussions can also work to connect the person facing the issue to the person solving it. The discussion section is very powerful, allowing comments, replies to comments and even replies to other replies.

Finally the app has a back-end that allows administrators and other privileged users to set the status tag on the feedback. This means that users can stay updated with the progress made on their feedback.

## Instructions
Although Amplio is pretty open to non-registered users, they are only silent spectators. To have any real say in the scheme of things, create an account. Your profile is very minimal, you just need to give your name, email (and an optional profile picture if you find the cryptographic identicons boring), we don't want any extra information. You however get a Student account by default. It can be upgraded by another privileged user as required.

The next step is to browse feedback and get some inspiration. See the kinds of feedback on the site. If you notice some issue or have some idea for the improvement of life in IIT Roorkee that is yet to be reported, you ought to do that yourself! Go to the compose page and submit your own feedback. If that idea has been reported already, just upvote it.

You can freely participate in discussions as well. Comment on the feedback, reply to an existing comment or reply and subscribe to comments or replies that you agree with.

## Instructions for running the application

* Clone the repository and `cd` into it.
* Make sure you've installed all the requirements specified. You can use `pip install requirements.txt` for it.
* The code right now is only compatible with PostgreSQL. If you want use MySQL or some other flavors of SQL, make changes in [settings.py](amplio_app/settings.py)
* You may encounter some more errors while running the app, most of them which are because of unavailability of python libraries.
* Run `python manage.py runserver <port_number>`
* You can also host it on your servers and have a good feedback system.

## Requirements
If you for some reason (I can't think of a single one) decide to clone this repository, you'll need a bunch of things to make it work.

### Python
Version 3.5.1

### PostgreSQL
Version 9.5

### Server
Apache2 
libapache2-mod-wsgi-py3

### PIP Packages
This is the output of pip freeze.

* dj-database-url==0.4.1
* Django==1.9.7
* gunicorn==19.6.0
* Pillow==3.3.0
* psycopg2==2.6.1
* validate-email==1.3
* whitenoise==3.2
