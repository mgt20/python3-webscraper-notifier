#!/usr/bin/python3

import bs4
import requests
import smtplib
import logging
import configparser
import http.client

logging.basicConfig(filename='log.log', filemode='w', level=logging.DEBUG)
pushover_conn = http.client.HTTPSConnection('api.pushover.net:443')

#ConfigParser configuration
config = configparser.ConfigParser()
config.read('/app/config.ini')

#ConfigParser variables import
notify_email = config.getboolean('notification', 'email')
notify_pushover = config.getboolean('notification', 'pushover')
toAddress = config.get('email', 'toAddress')
fromAddress = config.get('email', 'fromAddress')
fromPassword = config.get('email', 'fromPassword')
cssselector = config.get('css', 'cssselector')
searchterm = config.get('searchterm', 'keyword')
webpages = config.items('webpages')
pushover_user = config.get('pushover.net', 'PushoverUser')
pushover_token = config.get('pushover.net', 'PushoverToken')

def main():
    for key, website in webpages:
        getPage = requests.get(website)
        getPage.raise_for_status() #if error it will stop the program

        #Parse text for keyword
        menu = bs4.BeautifulSoup(getPage.text, 'html.parser')
        keywords = menu.select(cssselector)

        flength = len(searchterm)
        available = False

        for keyword in keywords:
            for i in range(len(keyword.text)):
                chunk = keyword.text[i:i+flength].lower()
                if chunk == searchterm:
                    available = True
        if available == True:
            if notify_email == True:
                conn = smtplib.SMTP('smtp.gmail.com', 587) # smtp address and port
                conn.ehlo() # call this to start the connection
                conn.starttls() # starts tls encryption. When we send our password it will be encrypted.
                conn.login(fromAddress, fromPassword)
                conn.sendmail(fromAddress, toAddress, 'Subject: python3-webscraper-notifier alert!\n\nAttention!\n\n ' + (searchterm) + ' is available today!\n\nVisit ' + (website) + ' to see it\n\npython3-webscraper-notifier V1.0')
                conn.quit()
                print('Sent notification e-mails for the following recipients:\n')
                for i in range(len(toAddress)):
                    print(toAddress[i])
                print('')
            if notify_pushover == True:
                r = requests.post("https://api.pushover.net/1/messages.json", data = {
                    "token": pushover_token,
                    "user": pushover_user,
                    "message": "Attention!\n\n " + (searchterm) + " is available today!\n\nVisit " + (website) + " to see it\n\npython3-webscraper-notifier V1.0"
                })
                print('Sent Pushover push notification')
        else:
            print('Your favorite item is not available today.')

# process main method call
if __name__ == '__main__':
    main()
