FROM python:alpine3.11

RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories && \
  apk add --no-cache git hub
  #Download the hub cli tool 
ADD main.py /
ADD createtmpbranch.sh /

RUN chmod 777 /createtmpbranch.sh

CMD ["python","./main.py"]