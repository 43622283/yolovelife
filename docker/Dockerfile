FROM python:3.6-alpine
MAINTAINER Yo YoLoveLife@outlook.com

RUN mkdir -p /app
COPY ./ /app/
COPY repositories /etc/apk/repositories
COPY pip.conf /root/.pip/pip.conf
RUN apk update \
	&& apk add openssl-dev \
	&& apk add openldap-dev \
	&& apk add mariadb-dev \
	&& apk add gcc \
	&& apk add libffi-dev \
	&& apk add musl-dev \
	&& apk add make \
	&& apk add libjpeg \
	&& apk add libjpeg-turbo-dev
RUN pip install -r /app/requirements.txt
WORKDIR /app
EXPOSE 8000
CMD [ "sh", "./init.sh"]
