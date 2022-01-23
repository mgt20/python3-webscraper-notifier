FROM python:3.9-alpine3.15

RUN apk update && \
    apk upgrade && \
    pip install bs4 requests

RUN mkdir -p app

WORKDIR /app

# Set pythonpath to the working directory of the container
ENV PYTHONPATH "${PYTHONPATH}:/app"

# Copy required files into the working directory of the container
COPY script.py script.py
COPY config.ini config.ini
COPY entrypoint.sh entrypoint.sh
COPY cronjobs /etc/crontabs/root

# Set permissions for files
#RUN chmod 644 /etc/cron.d/cronjobs 
RUN chmod a+x script.py entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
