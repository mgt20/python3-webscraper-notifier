# python3-webscraper-notifier 
A simple python3 script that sends an e-mail alert and/or Pushover notification if a desired item is on a webpage. Includes a Dockerfile which allows the script to run on a cron schedule inside of its own Docker container. 

This tool can look for specific text within a specific CSS element on several webpages and notify you when that text is present. 

### Pre-Requisites:
1. docker
2. docker-compose

## Options for Notifications

###Pushover.net
1. Using a computer, login to your pushover.net (note: this is a paid service) account
2. Copy "Your User Key", you will need to paste this into ```config.ini``` later
3. Click on "Create an Application/API Token"
4. Create a name for the new application and click on "Create Application"
5. Copy the "API Token/Key", you will need to paste this into ```config.ini``` later

###E-mail
1. The script is preconfigured to send email from a gmail account
2. You will need your account's username and password (an application key might be supported too, it hasn't been tested).

### To Use:
1. Rename ```config.sample.ini``` to ```config.ini``` (ex. ```mv config.sample.ini config.ini```)
2. Under the ```notifications``` section, set ```email_notify``` and/or ```pushover_notify``` to ```True``` if using those forms of notification, set the ones you don't plan to use to ```False```
3. If using email or Pushover, you will need to enter the specifics for those notification methods
4. Identify the webpage(s) to scrape
5. Use the Inspector feature in a web browser to find the CSS element that the text resides in. 
6. Modify config.ini file to add in the webpage(s) to scrape, the CSS element to look within, and the keywords to search for within that CSS element.
7. Modify the cron schedule within the ```cronjobs``` file to run the script how often you'd like. By default, the script is configured to run every 5 minutes (crontab.guru is a good tool to help figure this out).

### To Setup Docker Container and run the script on a schedule:
1. ```cd``` into the directory with the github repo on your machine
2. Run ```docker-compose up -d build``` to build the docker image from the Dockerfile and run it in Detached mode

