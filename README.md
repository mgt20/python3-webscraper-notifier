# python3-webscraper-emailer 
A simple python3 script that sends an e-mail alert if a desired item is on a webpage.

Pre-Requisites:
1. docker
2. docker-compose

To Use:

1. Identify the webpage to scrape
2. Use the Inspector feature in a web browser to find the CSS element that the text resides in. 
3. Modify the python script by replacing the variables after the "$"'s with your variables (email addresses, webpage url, css selector). Note: delete the $'s
4. Provide your sender account email address credentials, the script is pre-configured with gmail smtp information 
5. Run the script manually using syntax like "python3 python3-webscraper-emailer.py, test to ensure the script works manually

To Setup Docker Container and run the script on a schedule:
1. cd into the directory with the github repo on your machine
2. Run "docker-compose build" to build the docker image from the Dockerfile
3. Run "docker-compose up -d" to run the docker image in detached mode

NOTE:
- The cron schedule by default runs the script “At minute 0 past every 2nd hour from 8 through 17”. Modify this in the Dockerfile to adjust the schedule
