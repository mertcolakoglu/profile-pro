# pull official base image
FROM python:3.12-slim



# Update and install dependencies
RUN apt-get update

RUN apt-get install libpq-dev -y
RUN apt-get install python3-dev build-essential -y

# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV VIRTUAL_ENV=/opt/venv

# Upgrade pip and install virtualenv
RUN pip install --upgrade pip
RUN pip install virtualenv

# Create a virtual environment
RUN python -m virtualenv $VIRTUAL_ENV

# Ensure all subsequent commands run in the virtual environment
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install python dependencies
ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# Copy project files
COPY . /srv/app
WORKDIR /srv/app