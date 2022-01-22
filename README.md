# python3-webscraper-emailer 
A simple python3 script that sends an e-mail alert if a desired item is on a webpage. Includes a Dockerfile which allows the script to run on a cron schedule inside of its own Docker container. 

### Pre-Requisites:
1. docker
2. docker-compose

### To Use:

1. Identify the webpage to scrape
2. Use the Inspector feature in a web browser to find the CSS element that the text resides in. 
3. Rename ```config.sample.ini``` to ```config.ini``` (ex. ```mv config.sample.ini config.ini```)
4. Modify config.ini file to add in source email address, password, destination email address, the webpage(s) to scrape, the CSS element to look within, and the keywords to search for within that CSS element. The script is preconfigured to work with gmail's SMTP server information for the source email address account.
5. Modify the cron schedule within the ```cronjobs``` file to run the script how often you'd like. By default, the script is configured to run every 5 minutes (crontab.guru is a good tool to help figure this out).

### To Setup Docker Container and run the script on a schedule:
1. cd into the directory with the github repo on your machine
2. Run ```docker-compose build``` to build the docker image from the Dockerfile
3. Run ```docker-compose up -d``` to run the docker image in detached mode

