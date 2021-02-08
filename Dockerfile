FROM python:3.8.6

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip install pip==21.0.1 && \
    pip install -r requirements.txt
