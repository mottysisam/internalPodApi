# start by pulling the python image
FROM python:3.8-alpine

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# add curl
RUN apk --no-cache add curl

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

EXPOSE 5000
ENV FLASK_APP=pod_info_app/main.py

# configure the container to run in an executed manner
ENTRYPOINT [ "flask"]
CMD [ "run", "--host", "0.0.0.0" ]
