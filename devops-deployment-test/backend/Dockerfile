FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3 python3-dev python3-pip
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV FLASK_APP app.py
ENV FLASK_DEBUG 1
ENV VERSION 0.0.1
ENV NAME backend
ENV DBCONNETIONSTRING 'dbname=backend user=sammy password=sammypw host=postgresql port=5432'
EXPOSE 5001
CMD [ "python3", "-m", "flask", "run", "--port=5001", "--host=0.0.0.0" ]