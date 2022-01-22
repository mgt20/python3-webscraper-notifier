#!/usr/bin/python3
import bs4, requests, smtplib, logging, configparser

logging.basicConfig(filename='log.log', filemode='w', level=logging.DEBUG)

#ConfigParser configuration
config = configparser.ConfigParser()
config.read('/app/config.ini')

#ConfigParser variables import
toAddress = config.get('email', 'toAddress')
fromAddress = config.get('email', 'fromAddress')
fromPassword = config.get('email', 'fromPassword')
cssselector = config.get('css', 'cssselector')
searchterm = config.get('searchterm', 'keyword')
webpages = config.items('webpages')

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
        conn = smtplib.SMTP('smtp.gmail.com', 587) # smtp address and port
        conn.ehlo() # call this to start the connection
        conn.starttls() # starts tls encryption. When we send our password it will be encrypted.
        conn.login(fromAddress, fromPassword)
        conn.sendmail(fromAddress, toAddress, 'Subject: python3-webscraper-emailer alert!\n\nAttention!\n\n ' + (searchterm) + ' is available today!\n\nVisit ' + (website) + ' to see it\n\npython3-webscraper-emailer V1.0')
        conn.quit()
        print('Sent notification e-mails for the following recipients:\n')
        for i in range(len(toAddress)):
            print(toAddress[i])
        print('')
    else:
        print('Your favourite item is not available today.')
