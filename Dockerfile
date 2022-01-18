FROM python:3.9-alpine3.15
COPY python3-webscraper-emailer.py /python3-webscraper-emailer.py
# RUN echo "* * * * * echo hello" | crontab - 
RUN pip install bs4 requests

RUN echo "0 8-17/2 * * * python /python3-webscraper-emailer.py" | crontab -

CMD ["crond","-f"]
