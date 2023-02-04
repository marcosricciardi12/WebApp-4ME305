FROM python:latest

ADD app.py / 

ADD requirements.txt /

RUN pip install --upgrade pip

RUN pip3 install -r ./requirements.txt

CMD [ "python3", "./app.py]
