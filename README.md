# python3-webscraper-emailer 
A simple python3 script that sends an e-mail alert if a desired item is on a webpage.

To Use:

1. Identify the webpage to scrape
2. Use the Inspector feature in a web browser to find the CSS element that the text resides in. 
3. Modify the python script by replacing the variables after the "$"'s with your variables (email addresses, webpage url, css selector). Note: delete the $'s
4. Provide your sender account email address credentials, the script is pre-configured with gmail smtp information 
5. Run the script, test
6. Schedule the script with a tool like "cron" on Linux to run at predefined intervals you configure

This was derived and forked from baraolt/food-notifier

