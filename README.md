# Grow Lapse Server
Grow Lapse is an all in one software for managing timelapses.  This repo contains the server side code.  The server is written in python 2.7.  The map of the REST api can be found below

# Requirements
* Git
* Python 2.7
* PIP

# Installation
Clone and enter the repository:

`git clone https://github.com/HighTekGrow/growlapse-server.git`

`cd growlapse-serve`

Install python dependencies:

`pip install -r requirements.txt`

Copy template database:

`cp timelapse.db.template timelapse.db`

# Start The Server
From within the root of the growlapse-server directory enter the command:
`python growlapse.py`

# Client Installation
Check out the repo [here](https://github.com/HighTekGrow/growlapse-client) for information and instructions on getting the client setup.

# API Endpoints
#### /timelapse
- GET - Returns a list of all timelapses in the system currently
- POST - Create new timelapse. You must pass in the parameters below
   - name - Name of your time lapse
    - interval - Interval in seconds that teh system will take pictures
    - length - Length of timelapse in seconds
#### /timelapse/<time_lapse_id> 
- GET - Returns time lapse with the id provided
- DELETE - Deletes time lapse with provided id
#### /images
- GET - Returnes a list of all images currently in the system for all time lapses
#### /images/<image_id>
- GET - Returns the image with the given id 
#### /preview/<time_lapse_id>
- GET - Returns a GIF of the timelapse.  If the timelapse is still running it will generate a GIF with all images currently attached to the time lapse.  If it is not running a GIF of the entire time lapse will be returned 

--- 

Author: Sean Moriarty

Email: hightekgrow@gmail.com

Github: github.com/smoriarty21

Website: hightekco.com

Reddit: reddit.com/r/hightek/

Support HighTek: patreon.com/hightek

Donations: paypal.me/atarimaster