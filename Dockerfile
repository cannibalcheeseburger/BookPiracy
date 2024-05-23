FROM python:3.10-alpine

WORKDIR /app

RUN pip install requests beautifulsoup4 wget flask
RUN mkdir -p downloads
COPY app.py app.py
COPY ./templates ./templates

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]