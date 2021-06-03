FROM python

ADD requirements.txt /app/

WORKDIR /app

RUN pip install -r requirements.txt

ADD ./ /app/

RUN /app/airy*.json /root/

EXPOSE 8008

CMD ["sh", "./entry.sh"]
