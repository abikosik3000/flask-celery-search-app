FROM ubuntu:latest
MAINTAINER Nikolay Tsygankov 'abikosik2018@gmail.com'
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY . .
WORKDIR .
RUN pip install -r requirements.txt
CMD [ "celery" "multi" "start" "w1" "-A" "the_finder.celery.celery" "worker" "-l" "INFO" ]
CMD [ "flask", "--app" , "the_finder", "run", "--debug", "--host=0.0.0.0"]
# надо в thefinder.config надо указать доступ к базе redis, я не успеваю отладить 
# и проверить docker-compose.yml