FROM ubuntu:latest
MAINTAINER Nikolay Tsygankov 'abikosik2018@gmail.com'
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY . .
WORKDIR .
RUN pip install -r requirements.txt
#ENTRYPOINT ['python3']python3
#CMD ["export", "FLASK_APP=myapp"]
#CMD ["docker", "run" , "-d", "--name", "redis-stack", "-p", "6379:6379", "-p", "8001:8001", "redis/redis-stack"]
#CMD [ "flask", "--app" , "the_finder", "run", "--debug" ]