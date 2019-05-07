FROM python:3.6
MAINTAINER Yo YoLoveLife@outlook.com

COPY sources.list /etc/apt/sources.list
RUN apt-get clean \
	&& apt-get update -y --allow-unauthenticated \
	&& apt-get install libldap2-dev libsasl2-dev -y --allow-unauthenticated

RUN mkdir -p /app
COPY ./ /app/
COPY pip.conf /root/.pip/pip.conf
RUN pip install -r /app/requirements.txt
WORKDIR /app
EXPOSE 8000
CMD [ "sh", "./init.sh"]
