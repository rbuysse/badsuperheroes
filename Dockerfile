FROM alpine:latest

RUN apk update \
 && apk add \
    python \
    py-pip \
    git

RUN pip install pycorpora \
    tweepy

RUN git clone -b docker-data-dir https://github.com/rbuysse/twitterbot.git

WORKDIR twitterbot

RUN python setup.py install

RUN sed -i 's/logging.DEBUG/logging.INFO/' twitterbot/bot.py

RUN mkdir /data/

COPY *.py /twitterbot/
COPY data_files /twitterbot/data_files

CMD python herobot.py
