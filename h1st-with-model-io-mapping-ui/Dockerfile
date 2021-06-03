FROM python

ADD requirements.txt /app/

WORKDIR /app

RUN pip install -r requirements.txt

ADD ./ /app/

RUN cp /app/airy*.json ~/

EXPOSE 8008

CMD ["sh", "./entry.sh"]
