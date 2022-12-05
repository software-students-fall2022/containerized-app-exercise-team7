#base image
FROM python:3.9-bullseye

#set work directory insideimage
WORKDIR /web_app

# copy current dir contents into image dir
ADD . /web_app

#install requirments
RUN pip install --upgrade pip
RUN apt -y update
RUN apt-get install -y portaudio19-dev
RUN pip install -r requirements.txt


#listen to 5000 on at runtime
EXPOSE 5000

#run app when container launches
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]