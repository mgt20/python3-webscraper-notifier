#! python3
import bs4, requests, smtplib, logging

# ------------------- E-mail list ------------------------
toAddress = ['$destinationemailaddress@gmail.com']
# --------------------------------------------------------

webpage = '$https://webpageyouwanttoscrape.xyz/index.html'

logging.basicConfig(filename='log.log', filemode='w', level=logging.DEBUG)

#Download page
getPage = requests.get(webpage)
getPage.raise_for_status() #if error it will stop the program

#Parse text for keyword
menu = bs4.BeautifulSoup(getPage.text, 'html.parser')
keywords = menu.select('$cssselectorfrominspectingwebpage')

the_one = '$keywordtosearchfor' # This is the keyword to scrape the webpage for
flength = len(the_one)
available = False

for keyword in keywords:
    for i in range(len(keywords.text)):
        chunk = keyword.text[i:i+flength].lower()
        if chunk == the_one:
            available = True

if available == True:
    conn = smtplib.SMTP('smtp.gmail.com', 587) # smtp address and port
    conn.ehlo() # call this to start the connection
    conn.starttls() # starts tls encryption. When we send our password it will be encrypted.
    conn.login('$senderemailaddress@gmail.com', '$senderemailpasswordORappkey')
    conn.sendmail('youremail@gmail.com', toAddress, 'Subject: $This is the email subject!\n\nAttention!\n\nYour favourite item is available today!\n\nVisit ' + (webpage) + ' to see it\n\nNotifier V1.0')
    conn.quit()
    print('Sent notificaton e-mails for the following recipients:\n')
    for i in range(len(toAddress)):
        print(toAddress[i])
    print('')
else:
    print('Your favourite item is not available today.')
