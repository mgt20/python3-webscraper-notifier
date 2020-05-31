#! python3
import bs4, requests, smtplib, logging

logging.basicConfig(filename='log.log', filemode='w', level=logging.DEBUG)

## Configure these variables:
toAddress = ['$senttheemailtothisaddress@gmail.com']
# This is the email address you want to notify when there is a match
webpage = '$http://www.whateverwebsiteyouwant.xyz/items.html'
# This is the webpage you want to scrape
cssselector = '.$whatevercssselector-com-category-product-name'
# This is the CSS selector from the webpage where the keyword lives. It should begin with a "."
searchterm = '$whatwordshouldwelookfor'
# This is the keyword you are looking to match on the webpage
fromAddress = '$sendtheemailfromthisaddress@gmail.com'
# This is the email address we want to send the email from
fromPassword = '$mypasswordORappkey'
# This is the password or gmail app key (preferred) for the email address we are mailing from 
## End of Configuration

getPage = requests.get(webpage)
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
    conn.sendmail(fromAddress, toAddress, 'Subject: python3-webscraper-emailer alert!\n\nAttention!\n\nYour favorite item is available today!\n\nVisit ' + (webpage) + ' to see it\n\npython3-webscraper-emailer V1.0')
    conn.quit()
    print('Sent notificaton e-mails for the following recipients:\n')
    for i in range(len(toAddress)):
        print(toAddress[i])
    print('')
else:
    print('Your favourite item is not available today.')
